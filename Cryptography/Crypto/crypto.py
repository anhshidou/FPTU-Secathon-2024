import socket
import struct

def cipher(k, d):
    S = list(range(256))
    j = 0
    o = []
    for i in range(256):
        j = (j + S[i] + k[i % len(k)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    for c in d:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        o.append(c ^ S[(S[i] + S[j]) % 256])
    return bytearray(o)

def ip2d(ip_list):
    d = bytearray()
    for ip in ip_list:
        packed_ip = socket.inet_aton(ip)
        d.extend(packed_ip)
    return d

def decr(ipa, k):
    ed = ip2d(ipa)
    padding_length = ed[-1]
    ed = ed[:-padding_length]
    decrypted_data = cipher(k, ed)
    return decrypted_data.decode('utf-8')

def main():
    key = bytearray('supersecretkey', 'utf-8')
    ipa = ['159.96.34.204', '136.182.188.58', '155.20.31.30', '12.234.113.15', '153.170.118.69', '189.152.240.17', '180.27.111.161', '87.205.101.118', '45.1.136.2', '122.3.3.3']  # Đây là danh sách địa chỉ IP từ quá trình mã hóa
    decrypted_text = decr(ipa, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
