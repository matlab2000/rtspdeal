依赖于pypcap包,需要注意的是pcap.pyx中
    object PyBuffer_FromMemory(char *s, int len)
改成
    object PyString_FromStringAndSize(char *v, int len)
这样生成的包就不会使用同一个缓冲区了，否则处理后的包对应的地址都是同一个c内存
地址。不符合想把所有包读取到列表中的意图。

处理后输出的包是原始码流的包，如果需要处理成mp4容器格式的，可以使用mp4v2库

