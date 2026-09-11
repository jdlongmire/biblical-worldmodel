#!/usr/bin/env python3
"""Check responsive landing, navigation, actual search and mathematical rendering."""
import argparse,json,mimetypes
from pathlib import Path
from urllib.parse import urlsplit,unquote
from playwright.sync_api import sync_playwright
parser=argparse.ArgumentParser()
parser.add_argument('--url',default='https://jdlongmire.github.io/biblical-worldmodel/')
parser.add_argument('--built-root',type=Path)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=True)
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    context=browser.new_context();errors=[];missing=[]
    if args.built_root:
        def serve(route):
            path=unquote(urlsplit(route.request.url).path).removeprefix('/biblical-worldmodel/')
            target=args.built_root/path
            if target.is_dir():target=target/'index.html'
            if target.is_file():route.fulfill(path=str(target),content_type=mimetypes.guess_type(str(target))[0] or 'application/octet-stream')
            else:route.fulfill(status=404,body='missing')
        origin=urlsplit(args.url)
        context.route(f'{origin.scheme}://{origin.netloc}/**',serve)
    page=context.new_page();page.on('pageerror',lambda e:errors.append(str(e)))
    page.on('response',lambda r:missing.append(r.url) if r.status>=400 else None)
    for width,height,label in [(1440,1000,'desktop'),(768,1024,'tablet'),(390,844,'mobile'),(320,760,'small-mobile')]:
        page.set_viewport_size({'width':width,'height':height});page.goto(args.url,wait_until="domcontentloaded")
        page.locator('img').evaluate_all('(images)=>images.forEach(i=>i.loading="eager")')
        page.wait_for_function('Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)')
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),label
        assert page.locator('h1').count()==1
        assert page.locator('.audience-card').count()==4
        if label in ('desktop','mobile'):page.screenshot(path=str(args.output/(label+'.png')),full_page=True)
        if width<=760:
            page.get_by_role('button',name='Open navigation').click()
            assert page.locator('#main-nav').is_visible()
            page.keyboard.press('Escape');assert not page.locator('#main-nav').is_visible()
    page.set_viewport_size({'width':1440,'height':1000});page.goto(args.url,wait_until="domcontentloaded")
    page.get_by_role('button',name='Search the site').click()
    page.get_by_label('What would you like to explore?').fill('observation')
    page.locator('.search-dialog button[type=submit]').click()
    page.wait_for_selector('[data-md-component="search-result"] .md-search-result__item',timeout=30000)
    assert 'observation' in page.locator('[data-md-component="search-result"]').inner_text().lower()
    page.screenshot(path=str(args.output/'search.png'),full_page=False)
    page.goto(args.url+'methodology/',wait_until='domcontentloaded')
    page.wait_for_selector('mjx-container',timeout=30000)
    assert page.locator('mjx-container').count()>=3
    page.screenshot(path=str(args.output/'mathematics.png'),full_page=False)
    for route,title in [('start-here/','Start your journey'),('evidence/','Engage with the evidence'),('worldmodel/','Explore the Biblical WorldModel'),('objections/','Show us the strongest objections')]:
        response=page.goto(args.url+route,wait_until="domcontentloaded");assert response.status==200,route
        assert page.locator('h1').inner_text().strip()==title
    assert not errors,errors
    assert not missing,missing
    result={'url':args.url,'viewports':[1440,768,390,320],'responsive_overflow':'none','all_landing_images':'loaded','mobile_menu':'passed','search':'real observation results returned','mathematics':'rendered MathJax elements present','reader_routes':'4 passed','javascript_errors':errors,'http_errors':missing}
    (args.output/'browser-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
    browser.close()
