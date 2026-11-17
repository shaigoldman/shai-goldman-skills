#!/usr/bin/env python3
"""Extract page text blocks and coordinates as candidates, not verified paragraphs."""
import argparse,json
try:import fitz
except ImportError:raise SystemExit('PyMuPDF (fitz) is required; use a configured environment with it installed.')
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdf');p.add_argument('--output');a=p.parse_args();doc=fitz.open(a.pdf);pages=[]
 for i,page in enumerate(doc):
  blocks=[]
  for b in page.get_text('blocks'):
   if len(b)>6 and b[6]!=0:continue
   blocks.append({'bbox':[round(x,1) for x in b[:4]],'text':b[4].strip()})
  pages.append({'pdf_page':i+1,'width':page.rect.width,'height':page.rect.height,'blocks':blocks,'warning':'Extraction order, RTL text, columns, and paragraph numbers require visual verification.'})
 result=json.dumps({'file':a.pdf,'pages':pages},ensure_ascii=False,indent=2)
 if a.output:open(a.output,'w',encoding='utf8').write(result+'\n')
 else:print(result)
if __name__=='__main__':main()
