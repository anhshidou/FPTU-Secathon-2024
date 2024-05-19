# RE3

![image](https://github.com/anhshidou/FUSec2024/assets/120787381/40cf8890-7618-4634-ba88-74b21732079d)

Ban đầu khi mới sử dụng ida để xem file ELF, mình thấy rằng nó không hiện đầy đủ tất cả các hàm, mà chỉ xuất hiện các hàm sub ? Vậy nên mình nghĩ file này đã bị pack, lúc này mình unpack rồi xem lại

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  const char **v4; // [rsp+0h] [rbp-10h]

  v4 = argv;
  if ( argc != 3 || (argv = (const char **)"get_flag", (unsigned int)j_strcmp_ifunc(v4[1], "get_flag", envp)) )
  {
    puts("We are missing something here", argv, envp);
    return 1;
  }
  else
  {
    decrypt_flag(v4[2]);
    return 0;
  }
}
```

Xem đoạn pseududocode này, mình nhận thấy rằng nếu như truyền vào get_flag thì nó sẽ nhảy đến function decrypt_flag. Lúc này mình vào xem function decrypt_flag

```
unsigned __int64 __fastcall decrypt_flag(__int64 a1, __int64 a2, __int64 a3)
{
  __int64 v3; // rdx
  int v4; // r8d
  int v5; // r9d
  unsigned int i; // [rsp+1Ch] [rbp-34h]
  __int64 v8[3]; // [rsp+20h] [rbp-30h] BYREF
  char v9; // [rsp+38h] [rbp-18h]
  unsigned __int64 v10; // [rsp+48h] [rbp-8h]

  v10 = __readfsqword(0x28u);
  if ( (unsigned int)j_strcmp_ifunc(a1, "secretflagkey", a3) )
  {
    puts("Incorrect key. Try again.", "secretflagkey", v3);
  }
  else
  {
    v8[0] = encrypted_flag;
    v8[1] = qword_4C0168;
    v8[2] = qword_4C0170;
    v9 = byte_4C0178;
    for ( i = 0; i <= 0x17; i += 8 )
      substitute_and_permute((char *)v8 + (int)i);
    printf(
      (unsigned int)"Congratulations! Here is your flag: %s%s%s\n",
      (unsigned int)"FUSec{",
      (unsigned int)v8,
      (unsigned int)"}",
      v4,
      v5);
  }
  return __readfsqword(0x28u) ^ v10;
}
```

Mình nhận thấy rằng, nếu như string ở đây không phải là **secretflagkey** thì nó sẽ xuất ra dòng incorrect key, còn nếu là **secretflagkey** thì nó sẽ in ra flag. 

- Bởi vì: **j_strcmp_ifunc** đang so sánh với **a1** với string là **secretflagkey**

Sau khi đã nắm rõ được cách hoạt động, mình chạy file và thêm 2 string là **get_flag secretflagkey**

![image](https://github.com/anhshidou/FUSec2024/assets/120787381/d6ce78bb-fa42-4f0d-8039-6148fabb4692)

Flag: FUSec{Y0ugotm2friendscongrat}

- Done by anhshidou -







