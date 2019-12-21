Traffic seems to be from the Android phone 
- a lot of Google DNS 
- play.google.com DNS

Domain gvt1.com seems to be suspicious 
- https://www.virustotal.com/gui/domain/gvt1.com/details
- FEL directly involved https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-137-1/
-> False alarm it is google redirect domain https://www.systemtek.co.uk/2017/08/what-is-gvt1-com/
Or maybe not https://www.2-spyware.com/remove-redirector-gvt1-com.html

our packet analysis - https://packettotal.com/app/analysis?id=fb1f4903ca5852da9d6baf9b38c4afed

our host machine
- IPv4 - 10.0.2.15 
- IPv6 - fe80::353e:6fce:ee32:1a73
- it is member of multicast 224.0.0.252 - packet 9 | 239.255.255.250 - packet 46
- mac address - 08:00:27:40:76:00 (thats how i found out that this ipv4 is same as ipv6)
- robert pc - from packet 16
- it is running some service and advertising it on the multicast - found on packet 49
```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery" xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof" xmlns:pub="http://schemas.microsoft.com/windows/pub/2005/07">
  <soap:Header>
    <wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To>
    <wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Hello</wsa:Action>
    <wsa:MessageID>urn:uuid:1f8dd98d-9b04-43bc-ade9-a46fdaadef9c</wsa:MessageID>
    <wsd:AppSequence InstanceId="3" SequenceId="urn:uuid:0c646bf3-0987-47a3-b910-aa6494d712a9" MessageNumber="30"/>
  </soap:Header>
  <soap:Body>
    <wsd:Hello>
      <wsa:EndpointReference>
        <wsa:Address>urn:uuid:935d9a7b-90b5-4f96-a982-82533c923b47</wsa:Address>
      </wsa:EndpointReference>
      <wsd:Types>wsdp:Device pub:Computer</wsd:Types>
      <wsd:MetadataVersion>14</wsd:MetadataVersion>
    </wsd:Hello>
  </soap:Body>
</soap:Envelope>
```
- it is located on the `http://10.0.2.15:2869/upnphost/udhisapi.dll?content=uuid:a993d9e5-4f36-4a1d-8c6c-e890b15dfc07`
- `Server:Microsoft-Windows-NT/5.1 UPnP/1.0 UPnP-Device-Host/1.0`
- according to the 211 and probbaly previous packets, this device is running a windows server
```
Windows version: Windows 7 or Windows Server 2008 R2
Server Type: 0x00051003, Workstation, Server, NT Workstation, Potential Browser, Master Browser
```

There seems to be some file transfer? 1861-1862
-> 10.0.2.2 its MAC - 52:54:00:12:35:02

- 1868 - robert pc is leaving multicast group 224.0.0.252 -> it rejoined in 1879


---

weird packets 

HTTP/1.1 200 OK
Date: Tue, 01 May 2018 13:16:25 GMT
Server: Apache
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
Last-Modified: Fri, 19 Oct 2012 20:08:11 GMT
Accept-Ranges: bytes
Content-Length: 893
Cache-control: max-age=86400
Keep-Alive: timeout=5, max=100
Content-Type: application/x-pkcs7-mime

0y	*H÷
 j0f10	*H÷
 N0J02 D¯°Ö£'º09.ø@k0
	*H÷
0?1$0"U
Digital Signature Trust Co.10UDST Root CA X30
000930211219Z
210930140115Z0?1$0"U
Digital Signature Trust Co.10UDST Root CA X30"0
	*H÷
0
ß¯éPW´ÌbeöìÇÓ,k0Ê[ìÙÃ}Ç@Áàè3vI*ã?!I¬N¯>HËeîüÓ!eÒ*Ù2å÷w°{µÀ£©ºís.z2¢~0Í á*8¹y
1ýP½eß·QcÈâaêKaìRk¹¢âK(H£Ú	>.Ý ß[Æ*«.½pÅ%trÅ{j«4Ö0ÿåh{TÈÖ®ìZ=d³Æß¿ÉApìrÕ&ì8U9CÐüý\@ñëÕºÚ%¹ÆØßÁ:«Únñ>.õ\<Öiä*¶)Wãå=ð]£B0@0Uÿ0ÿ0Uÿ0UÄ§±¤{,qúÛáKuÿÄ`0
	*H÷
£,\©î(f7:¿Ç?KÃ	  ]ãÙYDÒ>
>½K tÎt~ÝËK³ DäéÌü}¥ÛjåþæýàNÝ·:µpI¯òåëñÑË:^HÄX_Zðñ±©ÜYnéõÊú¹f3ªY[Îâ§sGË+Ì°7HÏãVKõÏr2ÆðD»SrmCõ&HRg·X«þgvqxÛ
¢V9$1¢¨Z0GáÝP¼	ëdc`¼ÉæÒ}ù=2e´é|±WvêÅ¶(9¿eÈöwj
wØÛ)¶
î551