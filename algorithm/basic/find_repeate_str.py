# -*- coding: utf-8 -*-

class FirstRepeat:
    def __init__(self):
        pass

    def findFirstRepeat(self, A, n):
        """
        查找重复字符串
        :param A:
        :param n:
        :return:
        """
        for n1 in range(n):
            print n1
            for i, ch in enumerate(A[0:n1]):
                for j, ch1 in enumerate(A[i + 1:n1]):
                    if ch == ch1:
                        return ch


class Coder:
    def findCoder(self, A, n):
        # write code here
        result = list()
        positions = list()
        for i in range(n):
            if 'coder' in A[i]:
                result.append(A[i])
                length = len(A[i].split('coder')) - 1
                positions.append(length)
        for i in range(len(positions)-1, -1, -1):
            for j in range(0, i):
                if positions[j] < positions[j+1]:
                    tmp = positions[j]
                    tmp_result = result[j]
                    positions[j] = positions[j+1]
                    result[j] = result[j+1]
                    positions[j+1] = tmp
                    result[j+1] = tmp_result
        return result

if __name__ == '__main__':
    print FirstRepeat().findFirstRepeat('sadasas', 7)
    coder =["coder","quvnkcoderoscoderspxqcoderboxlscoderxtzhcoderxdnccoderqjwcoderduhcoderfewpwcoderlhwlcoderrkexcoderqmmbcoderfbcoderuscoderocoderdhgvpcoderuoocoderiwircoder","yngfcodervcoderrazxcoderwwbcoderxxkqvcoderiruzmcoderbxcoderchcoderddutcoderecoderkbmcoderzcoderhcoderfoocoder","focoderqbnacoderkmnuicoderimdcoderwkcoderqsyhcoderfuzqcoderzsncodersigocoder","lhkscoder","uscodersupcoderwuxlhcoderbzcodersskcoderaycoderlpcmcoderzgvcodertcodergcoderiqdcoderthpcoderkahzlcoderfucodericodervcoderywzlzcoderddcoder","jwywpcoderssmcoderdcpcodertubucoderitmucoder","oqvcodermrcoderoyecodertkecodergacoderlscoderrmcoderyuvccoderxcoderrnzmmcoderacoderhcoderijcoderjycoderkgycoder","scwpcoderbuffcoderdacoderfnacoderycodervjcoderkzcoderbcodertavphcoder","lxtcoderdgnjcoderyljvacodernwvcoderxdcodertmjgcoderjrvtcoderacoscodereqcoderdevjcoderdskhbcodertcoderccoder","xqoaxcoderwcoderrxcucoderplcodermmsjwcoderyfcoderscodervnacoder","vqicoderlcoderecoder","ccoderqeufcoderioozcoderkdtcoderyfojcodertfhicodervcoderqcoderdacoderapghcodervwscfcodernttcoderltbncoderecodermwcgcoderhqhtcoder","rcoderqyzgcoderyfdfcodermycoderibbfcoderqbescoderftoqocoderufblcodertcoderlbtkcoderutcoderbcoderwecoderdzpcoderrbmpcoderdcoderdcodericoderdlcoder","mvhncodervccoderczzcoderouajqcoderpcoderldcoderiuhmncoderwzdjcoderzocoderpcodergtfccoderocoderohipqcoderaveqccodertrgcoder","rqcoderygnpqcoderwwcodertjiikcodertmsghcoderacoderocoderrvyfxcoderyibaqcoderfvscodervocoderrwezocoderwecoderbefcoderqavcoderncoderaemvcoderyguncoder","pgicodergcoderfocoderefdhcoderdksdacoderwvnccoderuwscoderdzveccoderyvcodertmcoder","qmcoderfaqhcodercfcoderdcodercvrjmcoderixnykcoderzunsmcoderkwzcoderjdwcoderzacodervaglccoder","ncodersdnpcoderldcoderuzcodervqtdxcodertwcoderscoderecoderynntcodervalcoderdmacoderocoderbpkcoderfpvwtcoderjcoderpobscoder","shmcoderbimcoderuecoderfgzhxcodermcoderkuhhcodertlqcoderrcoderlrcoderhiehcoderbjxvlcoderycodercczlucoderizgdqcoderhcodersjcoderejwycoderwcodermocoderdcoder","pscodernvtwgcoder","kcodereewcoderrcoderzccoderkacodermbqaccoder","nbcodervzhscodergcoderanlwtcoderaepldcoderycciwcoderrorezcodermdcucoderxscoderryceecoderrlppcoderjncokcoderulccodergwcoderquvcoderhcoderhtcoderphyfcoderdobzcoder","kcoderxdqtcoder"]
    print Coder().findCoder(coder, 24)
