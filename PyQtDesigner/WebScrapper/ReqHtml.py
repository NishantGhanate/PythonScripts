from requests_html import HTMLSession
session = HTMLSession()
url = 'https://www.flipkart.com/mens-footwear/pr?count=40&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D699&p%5B%5D=sort%3Dpopularity&sid=osp%2Fcil&offer=nb:mp:08e0e6a129&fm=neo%2Fmerchandising&iid=M_4d538b55-a922-468b-8f37-0dff854c4bb1_3.FSXQIEK9KTMV&ppt=Homepage&ppn=Homepage&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_2_Under%2B%25E2%2582%25B9699%252BExtra%2B10%2525_FSXQIEK9KTMV_0&cid=FSXQIEK9KTMV'
r = session.get(url)
print(r.status_code)
# for html in r.html:
#     print(html)
    

print(r.html._next())
# print(r.html.links)
r = r.html.xpath('//*[@class="_1vC4OE"]//text()')
print(r)
