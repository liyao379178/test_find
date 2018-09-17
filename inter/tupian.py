from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "3f85994cc5a073165cbadf7d58618dad")
r.addBodyPara("typeId", "34")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"C:\\Users\\user\\Desktop\\5.png") #文件上传时设置
res = r.post()
test = res.json()["showapi_res_body"]["Result"]
print(test) # 返回信息