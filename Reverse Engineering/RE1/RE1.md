# Đề bài

![image](https://github.com/anhshidou/FUSec2024/assets/90485791/0207f96b-742b-4f3e-9920-52fc9b6263fd)

# Phân tích


Mở file bằng ida, bật hiển thị dưới dạng pseudo code, ta thấy:

Hàm `main`:
```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+8h] [rbp-278h]
  int v5; // [rsp+Ch] [rbp-274h]
  int v6; // [rsp+10h] [rbp-270h]
  int v7[40]; // [rsp+30h] [rbp-250h] BYREF
  int v8[40]; // [rsp+D0h] [rbp-1B0h] BYREF
  char s[264]; // [rsp+170h] [rbp-110h] BYREF
  unsigned __int64 v10; // [rsp+278h] [rbp-8h]

  v10 = __readfsqword(0x28u);
  v7[0] = 168;
  v7[1] = 193;
  v7[2] = 122;
  v7[3] = 172;
  v7[4] = 158;
  v7[5] = 108;
  v7[6] = 206;
  v7[7] = 153;
  v7[8] = 175;
  v7[9] = 175;
  v7[10] = 194;
  v7[11] = 189;
  v7[12] = 141;
  v7[13] = 127;
  v7[14] = 101;
  v7[15] = 202;
  v7[16] = 208;
  v7[17] = 116;
  v7[18] = 149;
  v7[19] = 160;
  v7[20] = 146;
  v7[21] = 179;
  v7[22] = 114;
  v7[23] = 143;
  v7[24] = 187;
  v7[25] = 159;
  v7[26] = 126;
  v7[27] = 109;
  v7[28] = 174;
  v7[29] = 156;
  v7[30] = 185;
  v7[31] = 120;
  v7[32] = 164;
  v7[33] = 189;
  v7[34] = 112;
  v7[35] = 120;
  v7[36] = 123;
  v7[37] = 145;
  v8[0] = 53;
  v8[1] = 87;
  v8[2] = 22;
  v8[3] = 73;
  v8[4] = 48;
  v8[5] = 1;
  v8[6] = 91;
  v8[7] = 53;
  v8[8] = 58;
  v8[9] = 62;
  v8[10] = 89;
  v8[11] = 74;
  v8[12] = 35;
  v8[13] = 28;
  v8[14] = 1;
  v8[15] = 92;
  v8[16] = 99;
  v8[17] = 17;
  v8[18] = 41;
  v8[19] = 45;
  v8[20] = 29;
  v8[21] = 79;
  v8[22] = 10;
  v8[23] = 44;
  v8[24] = 68;
  v8[25] = 58;
  v8[26] = 11;
  v8[27] = 12;
  v8[28] = 72;
  v8[29] = 38;
  v8[30] = 83;
  v8[31] = 2;
  v8[32] = 67;
  v8[33] = 74;
  v8[34] = 12;
  v8[35] = 5;
  v8[36] = 23;
  v8[37] = 45;
  printf("Enter the license key: ");
  fgets(s, 256, _bss_start);
  if ( s[strlen(s) - 1] == 10 )
    s[strlen(s) - 1] = 0;
  v4 = strlen("FUSec{");
  v5 = strlen("}");
  v6 = strlen(s);
  if ( v6 > v4 + v5 && !strncmp(s, "FUSec{", v4) && !strncmp(&s[v6 - (__int64)v5], "}", v5) && v6 - v4 - v5 == 38 )
  {
    if ( (unsigned __int8)check_license_key(&s[v4], v7, v8, 38LL) )
      puts("Correct key!");
    else
      puts("Incorrect key.");
    return 0;
  }
  else
  {
    puts("Incorrect key.");
    return 0;
  }
}

```

Hàm `check_license_key`:
```
__int64 __fastcall check_license_key(__int64 a1, __int64 a2, __int64 a3, int a4)
{
  int i; // [rsp+28h] [rbp-4h]

  for ( i = 0; i < a4; ++i )
  {
    if ( *(_BYTE *)(i + a1) != *(_BYTE *)(4LL * i + a2) - *(_BYTE *)(4LL * i + a3) )
      return 0LL;
  }
  return 1LL;
}
```
Trong hàm main gọi hàm `check_license_key` với các tham số &s[v4], v7, v8, 38LL; ta sẽ check hàm `check_license_key` với các tham số tương ứng.

Tại đấy, ta thấy rằng nếu i + &s[v4] = (4LL * i + v7) - (4LL * i + v8) trong 38 lần check (lặp từ i = 0 đến i = 38) thì hàm sẽ trả về true. Do đó ta biết được token sẽ là v7[i] trừ v8[i] với i chạy từ 0 đến 37.
Mặt khác do ở `main` gọi hàm `check_license_key` với kiểu dữ liệu (unsigned __int8) mà token lại là string, nên ta cần chuyển đổi từ số (kết quả của v7 -v8) về string.

#Lời giải

```
v7 = [168, 193, 122, 172, 158, 108, 206, 153, 175, 175, 194, 189, 141, 127, 101, 202, 208, 116, 149, 160, 146, 179, 114, 143, 187, 159, 126, 109, 174, 156, 185, 120, 164, 189, 112, 120, 123, 145]
v8 = [53, 87, 22, 73, 48, 1, 91, 53, 58, 62, 89, 74, 35, 28, 1, 92, 99, 17, 41, 45, 29, 79, 10, 44, 68, 58, 11, 12, 72, 38, 83, 2, 67, 74, 12, 5, 23, 45]

token = []

#Tính ra phần token từ v7 và v8
for i in range(38):
    token.append(chr(v7[i] - v8[i]))

#Convert the list of characters to a string
token_string = ''.join(key_main_part)

#Form the full key
flag = "FUSec{" + token_string + "}"

print(flag)
```

# Flag

FUSec{sjdcnksduqisjcdnmclsudhcwesafvfvasdsdd}
