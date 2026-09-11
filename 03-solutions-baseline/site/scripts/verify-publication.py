#!/usr/bin/env python3
"""Bind a successful hosted Pages run to its source SHA and live public response."""
import argparse,json,subprocess,urllib.request
parser=argparse.ArgumentParser()
parser.add_argument('--run-id',required=True)
parser.add_argument('--sha',required=True)
args=parser.parse_args()
repo='jdlongmire/biblical-worldmodel'
def api(path):return json.loads(subprocess.check_output(['gh','api',path],text=True))
run=api(f'repos/{repo}/actions/runs/{args.run_id}')
assert run['head_sha']==args.sha and run['conclusion']=='success',run.get('conclusion')
jobs=api(f'repos/{repo}/actions/runs/{args.run_id}/jobs')['jobs']
assert any(j['name']=='build' and j['conclusion']=='success' for j in jobs)
assert any(j['name']=='deploy' and j['conclusion']=='success' for j in jobs)
assert all(j.get('runner_name','').startswith('GitHub Actions') for j in jobs),[(j['name'],j.get('runner_name')) for j in jobs]
settings=api(f'repos/{repo}/pages');assert settings['build_type']=='workflow'
url=settings['html_url']
with urllib.request.urlopen(url,timeout=30) as response:
    body=response.read().decode();assert response.status==200
    assert 'A Coherent View' in body and 'audience-card' in body
print(json.dumps({'source_sha':args.sha,'actions_run':run['html_url'],'url':url,'hosted_build_and_deploy':'success','live_status':200}))
