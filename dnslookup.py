# make sure you have dnspython installed with 'pip3 install dnspython'
# final command should end up something like this: 'python3 dnslookup.py example.com'

import dns.resolver
import sys


def lookup(domain):
    types = [
        'NONE',
        'A',
        'NS',
        'MD',
        'MF',
        'CNAME',
        'SOA',
        'MB',
        'MG',
        'MR',
        'NULL',
        'WKS',
        'PTR',
        'HINFO',
        'MINFO',
        'MX',
        'TXT',
        'RP',
        'AFSDB',
        'X25',
        'ISDN',
        'RT',
        'NSAP',
        'NSAP-PTR',
        'SIG',
        'KEY',
        'PX',
        'GPOS',
        'AAAA',
        'LOC',
        'NXT',
        'SRV',
        'NAPTR',
        'KX',
        'CERT',
        'A6',
        'DNAME',
        'OPT',
        'APL',
        'DS',
        'SSHFP',
        'IPSECKEY',
        'RRSIG',
        'NSEC',
        'DNSKEY',
        'DHCID',
        'NSEC3',
        'NSEC3PARAM',
        'TLSA',
        'HIP',
        'CDS',
        'CDNSKEY',
        'CSYNC',
        'SPF',
        'UNSPEC',
        'EUI48',
        'EUI64',
        'TKEY',
        'TSIG',
        'IXFR',
        'AXFR',
        'MAILB',
        'MAILA',
        'ANY',
        'URI',
        'CAA',
        'TA',
        'DLV',
    ]
    
    for x in types:
        try:
            res = dns.resolver.resolve(domain, x)
            for y in res:
                print("#", x, ':', y.to_text())
            print()
    
        except Exception as e:
            pass

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("invalid input, try again.")
    else: 
        print()
        print()
        print("###############################################")
        print("#              DNS LOOKUP V0.2                #")
        print("#              CHASE EDSON 2022               #")
        print("###############################################")
        print()
        print()
        lookup(sys.argv[1])


















