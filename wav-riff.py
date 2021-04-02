import struct
import io

class WAVFile:

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with io.open(self.filename, 'rb') as fh:
            riff, size, fformat = struct.unpack('<4sI4s', fh.read(12))
            print("Riff: %s, Chunk Size: %i, format: %s" % (riff, size, fformat))

            # Read header
            chunk_header = fh.read(8)
            subchunkid, subchunksize = struct.unpack('<4sI', chunk_header)

            if (subchunkid == b'fmt '):
                aformat, channels, samplerate, byterate, blockalign, bps = struct.unpack('HHIIHH', fh.read(16))
                bitrate = (samplerate * channels * bps) / 1024
                print("Format: %i, Channels %i, Sample Rate: %i, Kbps: %i" % (aformat, channels, samplerate, bitrate))

            chunkOffset = fh.tell()
            while (chunkOffset < size):
                fh.seek(chunkOffset)
                subchunk2id, subchunk2size = struct.unpack('<4sI', fh.read(8))
                print("chunk id: %s, size: %i" % (subchunk2id, subchunk2size))
                if (subchunk2id == b'LIST'):
                    listtype = struct.unpack('<4s', fh.read(4))
                    print("\tList Type: %s, List Size: %i" % (listtype, subchunk2size))

                    listOffset = 0;
                    while ((subchunk2size - 8) >= listOffset):
                        listitemid, listitemsize = struct.unpack('<4sI', fh.read(8))
                        listOffset = listOffset + listitemsize + 8
                        listdata = fh.read(listitemsize)
                        print("\tList id %s, size: %i, data: %s" % (
                        listitemid.decode('ascii'), listitemsize, listdata))
                        print("\tOffset: %i" % listOffset)
                elif (subchunk2id == b'data'):
                    print("Found data")
                else:
                    print("Data: %s" % fh.read(subchunk2size).decode('ascii'))

                chunkOffset = chunkOffset + subchunk2size + 8


wavFile = WAVFile('test.wav')
wavFile.read()