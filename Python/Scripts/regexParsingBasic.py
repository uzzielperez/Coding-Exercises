import re

line ="""Subject:
    Security ID:        S-1-5-21-3368353891-1012177287-890106238-22451
    Account Name:       ChamaraKer
    Account Domain:     JIC
    Logon ID:       0x1fffb

Object:
    Object Server:  Security
    Object Type:    File
    Object Name:    D:\ApacheTomcat\apache-tomcat-6.0.36\logs\localhost.2013-07-01.log
    Handle ID:  0x11dc"""

regex = (r'Object Name:\s+(.*)')
match1 = re.findall(regex,line)
#print (match1)

xsecSection = """
*-------  PYTHIA Event and Cross Section Statistics  -------------------------------------------------------------*
 |                                                                                                                 |
 | Subprocess                                    Code |            Number of events       |      sigma +- delta    |
 |                                                    |       Tried   Selected   Accepted |     (estimated) (mb)   |
 |                                                    |                                   |                        |
 |-----------------------------------------------------------------------------------------------------------------|
 |                                                    |                                   |                        |
 | f fbar -> (LED G*) -> gamma gamma             5026 |        3743        775        775 |   8.458e-12  1.373e-13 |
 | g g -> (LED G*) -> gamma gamma                5027 |        2896        225        225 |   2.249e-12  7.391e-14 |
 |                                                    |                                   |                        |
 | sum                                                |        6639       1000       1000 |   1.071e-11  1.560e-13 |
 |                                                                                                                 |
 *-------  End PYTHIA Event and Cross Section Statistics ----------------------------------------------------------*
 """

regex2 = (r'sum\s+(.*)')
match2 = re.findall(regex2, xsecSection)
match2 = match2[0].split(" ")
#a = str(match2[0])
#a = a.split(" ")
print match2
#print (a) 
error = match2[-2]
xsec = match2[-4]
print "xsec (mb): ", xsec, "delta (mb)", error 
