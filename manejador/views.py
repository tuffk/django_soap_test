from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    template = loader.get_template('manejador/index.html')
    data = {
        'questions': Question.objects.all()
    }
    return HttpResponse(template.render(data, request))


def soapsl(request):
    import zeep
    from lxml import etree
    wsdl = 'https://api.smdservers.net/CCWs_3.5/CallCenterWs.asmx?WSDL'
    client = zeep.Client(wsdl=wsdl)

    ans = client.service.SiteInformation(sCorpCode="CCTST",
                                         sLocationCode="Demo",
                                         sCorpUserName="Administrator:::WAKE63JD73HNF6R5N3FG",
                                         sCorpPassword="Demo")
    # result = ans.SiteInformationResult
    result = etree.tostring(ans._value_1, pretty_print=True)
    # import pdb; pdb.set_trace()
    for i in ans._value_1.getiterator():
        print(f'{i.tag} - {i.text}\n')
    return HttpResponse(result)


def soapsl2(request):
    import zeep
    from lxml import etree
    wsdl = 'https://api.smdservers.net/CCWs_3.5/CallCenterWs.asmx?WSDL'
    client = zeep.Client(wsdl=wsdl)

    ans = client.service.TenantLogin(sCorpCode="CCTST",
                                     sLocationCode="Demo",
                                     sCorpUserName="Administrator:::WAKE63JD73HNF6R5N3FG",
                                     sCorpPassword="Demo",
                                     sTenantLogin="mimail@gmail.com",
                                     sTenantPassword="123456789")
    result = etree.tostring(ans._value_1, pretty_print=True)
    kuz = ans._value_1.xpath("//RT")
    for x in kuz:
        print("usuario")
        for y in x.getiterator():
            print(f"\t{y.tag} - {y.text}")
    # import pdb; pdb.set_trace()
    return HttpResponse(result)
