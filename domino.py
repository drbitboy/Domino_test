### Domino printer protocol
###
### Cf. https://www.plctalk.net/qanda//attachment.php?attachmentid=58296&d=1621049542

STX,LF,CR,ETB,SOH,ETX = map(chr,(0x02,0x0a,0x0d,0x17,0x01,0x03,))

def encode_data_850(layout,vardata_sequence):
  vardata = LF.join(vardata_sequence)
  pre_checksum = f"{STX}041C1E{layout}Q1{ETB}D{vardata}"
  checksum = '{0:02X}'.format(sum([ord(s) for s in pre_checksum[1:]]))[-2:]
  return (f"{pre_checksum}{checksum}{CR}").encode('cp850')

def decode_data_850(encoded_string):
  return encoded_string.decode('cp850').replace(STX,'<STX>'
                                      ).replace(LF,'<LF>'
                                      ).replace(CR,'<CR>'
                                      ).replace(ETB,'<ETB>'
                                      ).replace(SOH,'<SOH>'
                                      ).replace(ETX,'<ETX>'
                                      )
