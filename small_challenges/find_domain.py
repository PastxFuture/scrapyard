# Write a function to find the domain name from the IP address. 
# The function will accept an IP address, make a DNS request, and return the domain name that maps to that IP address while using records of PTR DNS.
# You can import the Python socket library.

# importing socket module
import socket

def find_domain(ip_address):
    host = socket.gethostbyaddr(ip_address)

    #split_domain = host[0].split('.')

    #domain = f'{split_domain[2]}.{split_domain[3]}'

    return host[0]

print(find_domain('86.191.110.15'))