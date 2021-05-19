### Domino printer protocol
###
### Cf. https://www.plctalk.net/qanda//attachment.php?attachmentid=58296&d=1621049542

STX,LF,CR,ETB,SOH,ETX = map(chr,(0x02,0x0a,0x0d,0x17,0x01,0x03,))

def calculate_checksum_string(pre_checksum):
  return '{0:02X}'.format(sum([b for b in pre_checksum.encode(encoding='cp850')]))[-2:]

def encode_data_850(layout,vardata_sequence):
  vardata = LF.join(vardata_sequence)
  pre_checksum = f"{STX}041C1E{layout}Q1{ETB}D{vardata}"
  checksum = calculate_checksum_string(pre_checksum[1:])
  return (f"{pre_checksum}{checksum}{CR}").encode(encoding='cp850')

def decode_data_850(encoded_string):
  return encoded_string.decode(encoding='cp850').replace(STX,'<STX>'
                                               ).replace(LF,'<LF>'
                                               ).replace(CR,'<CR>'
                                               ).replace(ETB,'<ETB>'
                                               ).replace(SOH,'<SOH>'
                                               ).replace(ETX,'<ETX>'
                                               )

def checksum_is_valid(encoded_data):
  source_checksum = encoded_data[-3:-1].decode(encoding='cp850')
  calculated_checksum = calculate_checksum_string(encoded_data[1:-3].decode(encoding='cp850'))
  return source_checksum == calculated_checksum,source_checksum,calculated_checksum
  
