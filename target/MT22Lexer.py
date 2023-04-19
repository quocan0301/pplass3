# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01c3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\7\2\u0084")
        buf.write("\n\2\f\2\16\2\u0087\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\7\3\u0092\n\3\f\3\16\3\u0095\13\3\3\3\3\3\3\4\6")
        buf.write("\4\u009a\n\4\r\4\16\4\u009b\3\4\3\4\3\5\3\5\3\5\5\5\u00a3")
        buf.write("\n\5\3\6\3\6\5\6\u00a7\n\6\3\7\3\7\3\7\3\b\3\b\3\b\5\b")
        buf.write("\u00af\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.")
        buf.write("\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\5\66\u015d\n\66\3\66\7\66\u0160\n")
        buf.write("\66\f\66\16\66\u0163\13\66\3\67\3\67\7\67\u0167\n\67\f")
        buf.write("\67\16\67\u016a\13\67\3\67\3\67\3\67\7\67\u016f\n\67\f")
        buf.write("\67\16\67\u0172\13\67\7\67\u0174\n\67\f\67\16\67\u0177")
        buf.write("\13\67\3\67\5\67\u017a\n\67\3\67\3\67\38\38\38\38\38\3")
        buf.write("8\38\38\38\38\58\u0188\n8\38\38\39\39\39\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\5:\u0197\n:\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u01a2")
        buf.write("\n;\3<\3<\7<\u01a6\n<\f<\16<\u01a9\13<\3<\3<\3<\3=\3=")
        buf.write("\3=\3>\3>\7>\u01b3\n>\f>\16>\u01b6\13>\3>\3>\3?\3?\7?")
        buf.write("\u01bc\n?\f?\16?\u01bf\13?\3?\3?\3?\3\u0085\2@\3\3\5\4")
        buf.write("\7\5\t\2\13\2\r\2\17\2\21\6\23\7\25\b\27\t\31\n\33\13")
        buf.write("\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/\25\61\26\63\27")
        buf.write("\65\30\67\319\32;\33=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'")
        buf.write("U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65q\66s\67u8w9y")
        buf.write(":{;}<\3\2\13\4\2\f\f\17\17\5\2\n\f\16\17\"\"\3\2\62;\7")
        buf.write("\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\3\2\63;\4\2GGgg\2\u01d1\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\3\177\3\2\2\2\5\u008d\3\2\2\2\7\u0099\3\2\2\2\t")
        buf.write("\u00a2\3\2\2\2\13\u00a6\3\2\2\2\r\u00a8\3\2\2\2\17\u00ae")
        buf.write("\3\2\2\2\21\u00b0\3\2\2\2\23\u00b5\3\2\2\2\25\u00bb\3")
        buf.write("\2\2\2\27\u00c3\3\2\2\2\31\u00c6\3\2\2\2\33\u00cb\3\2")
        buf.write("\2\2\35\u00d1\3\2\2\2\37\u00d5\3\2\2\2!\u00de\3\2\2\2")
        buf.write("#\u00e1\3\2\2\2%\u00e9\3\2\2\2\'\u00f0\3\2\2\2)\u00f7")
        buf.write("\3\2\2\2+\u00fd\3\2\2\2-\u0102\3\2\2\2/\u0106\3\2\2\2")
        buf.write("\61\u010f\3\2\2\2\63\u0112\3\2\2\2\65\u011a\3\2\2\2\67")
        buf.write("\u0120\3\2\2\29\u0122\3\2\2\2;\u0124\3\2\2\2=\u0126\3")
        buf.write("\2\2\2?\u0128\3\2\2\2A\u012a\3\2\2\2C\u012c\3\2\2\2E\u012f")
        buf.write("\3\2\2\2G\u0132\3\2\2\2I\u0135\3\2\2\2K\u0138\3\2\2\2")
        buf.write("M\u013a\3\2\2\2O\u013d\3\2\2\2Q\u013f\3\2\2\2S\u0142\3")
        buf.write("\2\2\2U\u0145\3\2\2\2W\u0147\3\2\2\2Y\u0149\3\2\2\2[\u014b")
        buf.write("\3\2\2\2]\u014d\3\2\2\2_\u014f\3\2\2\2a\u0151\3\2\2\2")
        buf.write("c\u0153\3\2\2\2e\u0155\3\2\2\2g\u0157\3\2\2\2i\u0159\3")
        buf.write("\2\2\2k\u015c\3\2\2\2m\u0179\3\2\2\2o\u0187\3\2\2\2q\u018b")
        buf.write("\3\2\2\2s\u0196\3\2\2\2u\u01a1\3\2\2\2w\u01a3\3\2\2\2")
        buf.write("y\u01ad\3\2\2\2{\u01b0\3\2\2\2}\u01b9\3\2\2\2\177\u0080")
        buf.write("\7\61\2\2\u0080\u0081\7,\2\2\u0081\u0085\3\2\2\2\u0082")
        buf.write("\u0084\13\2\2\2\u0083\u0082\3\2\2\2\u0084\u0087\3\2\2")
        buf.write("\2\u0085\u0086\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0088")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\7,\2\2\u0089")
        buf.write("\u008a\7\61\2\2\u008a\u008b\3\2\2\2\u008b\u008c\b\2\2")
        buf.write("\2\u008c\4\3\2\2\2\u008d\u008e\7\61\2\2\u008e\u008f\7")
        buf.write("\61\2\2\u008f\u0093\3\2\2\2\u0090\u0092\n\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093\3")
        buf.write("\2\2\2\u0096\u0097\b\3\2\2\u0097\6\3\2\2\2\u0098\u009a")
        buf.write("\t\3\2\2\u0099\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009d\u009e\b\4\2\2\u009e\b\3\2\2\2\u009f\u00a0\t\4\2")
        buf.write("\2\u00a0\u00a3\5\t\5\2\u00a1\u00a3\t\4\2\2\u00a2\u009f")
        buf.write("\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\n\3\2\2\2\u00a4\u00a7")
        buf.write("\n\5\2\2\u00a5\u00a7\5\r\7\2\u00a6\u00a4\3\2\2\2\u00a6")
        buf.write("\u00a5\3\2\2\2\u00a7\f\3\2\2\2\u00a8\u00a9\7^\2\2\u00a9")
        buf.write("\u00aa\t\6\2\2\u00aa\16\3\2\2\2\u00ab\u00ac\7^\2\2\u00ac")
        buf.write("\u00af\n\6\2\2\u00ad\u00af\7^\2\2\u00ae\u00ab\3\2\2\2")
        buf.write("\u00ae\u00ad\3\2\2\2\u00af\20\3\2\2\2\u00b0\u00b1\7c\2")
        buf.write("\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7")
        buf.write("q\2\2\u00b4\22\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba")
        buf.write("\7m\2\2\u00ba\24\3\2\2\2\u00bb\u00bc\7d\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7q\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7p\2\2\u00c2\26")
        buf.write("\3\2\2\2\u00c3\u00c4\7f\2\2\u00c4\u00c5\7q\2\2\u00c5\30")
        buf.write("\3\2\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9")
        buf.write("\7u\2\2\u00c9\u00ca\7g\2\2\u00ca\32\3\2\2\2\u00cb\u00cc")
        buf.write("\7h\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7c\2\2\u00cf\u00d0\7v\2\2\u00d0\34\3\2\2\2\u00d1\u00d2")
        buf.write("\7h\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7t\2\2\u00d4\36")
        buf.write("\3\2\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7\7w\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7k\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7p\2\2\u00dd \3")
        buf.write("\2\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7h\2\2\u00e0\"\3")
        buf.write("\2\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7i\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\u00e8\7t\2\2\u00e8$\3\2\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7w\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7p\2\2\u00ef&\3")
        buf.write("\2\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6")
        buf.write("\7i\2\2\u00f6(\3\2\2\2\u00f7\u00f8\7y\2\2\u00f8\u00f9")
        buf.write("\7j\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc*\3\2\2\2\u00fd\u00fe\7x\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7f\2\2\u0101,\3")
        buf.write("\2\2\2\u0102\u0103\7q\2\2\u0103\u0104\7w\2\2\u0104\u0105")
        buf.write("\7v\2\2\u0105.\3\2\2\2\u0106\u0107\7e\2\2\u0107\u0108")
        buf.write("\7q\2\2\u0108\u0109\7p\2\2\u0109\u010a\7v\2\2\u010a\u010b")
        buf.write("\7k\2\2\u010b\u010c\7p\2\2\u010c\u010d\7w\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e\60\3\2\2\2\u010f\u0110\7q\2\2\u0110\u0111")
        buf.write("\7h\2\2\u0111\62\3\2\2\2\u0112\u0113\7k\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\u0115\7j\2\2\u0115\u0116\7g\2\2\u0116\u0117")
        buf.write("\7t\2\2\u0117\u0118\7k\2\2\u0118\u0119\7v\2\2\u0119\64")
        buf.write("\3\2\2\2\u011a\u011b\7c\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7t\2\2\u011d\u011e\7c\2\2\u011e\u011f\7{\2\2\u011f\66")
        buf.write("\3\2\2\2\u0120\u0121\7-\2\2\u01218\3\2\2\2\u0122\u0123")
        buf.write("\7/\2\2\u0123:\3\2\2\2\u0124\u0125\7,\2\2\u0125<\3\2\2")
        buf.write("\2\u0126\u0127\7\61\2\2\u0127>\3\2\2\2\u0128\u0129\7\'")
        buf.write("\2\2\u0129@\3\2\2\2\u012a\u012b\7#\2\2\u012bB\3\2\2\2")
        buf.write("\u012c\u012d\7(\2\2\u012d\u012e\7(\2\2\u012eD\3\2\2\2")
        buf.write("\u012f\u0130\7~\2\2\u0130\u0131\7~\2\2\u0131F\3\2\2\2")
        buf.write("\u0132\u0133\7?\2\2\u0133\u0134\7?\2\2\u0134H\3\2\2\2")
        buf.write("\u0135\u0136\7#\2\2\u0136\u0137\7?\2\2\u0137J\3\2\2\2")
        buf.write("\u0138\u0139\7>\2\2\u0139L\3\2\2\2\u013a\u013b\7>\2\2")
        buf.write("\u013b\u013c\7?\2\2\u013cN\3\2\2\2\u013d\u013e\7@\2\2")
        buf.write("\u013eP\3\2\2\2\u013f\u0140\7@\2\2\u0140\u0141\7?\2\2")
        buf.write("\u0141R\3\2\2\2\u0142\u0143\7<\2\2\u0143\u0144\7<\2\2")
        buf.write("\u0144T\3\2\2\2\u0145\u0146\7*\2\2\u0146V\3\2\2\2\u0147")
        buf.write("\u0148\7+\2\2\u0148X\3\2\2\2\u0149\u014a\7}\2\2\u014a")
        buf.write("Z\3\2\2\2\u014b\u014c\7\177\2\2\u014c\\\3\2\2\2\u014d")
        buf.write("\u014e\7]\2\2\u014e^\3\2\2\2\u014f\u0150\7_\2\2\u0150")
        buf.write("`\3\2\2\2\u0151\u0152\7?\2\2\u0152b\3\2\2\2\u0153\u0154")
        buf.write("\7.\2\2\u0154d\3\2\2\2\u0155\u0156\7\60\2\2\u0156f\3\2")
        buf.write("\2\2\u0157\u0158\7=\2\2\u0158h\3\2\2\2\u0159\u015a\7<")
        buf.write("\2\2\u015aj\3\2\2\2\u015b\u015d\t\7\2\2\u015c\u015b\3")
        buf.write("\2\2\2\u015d\u0161\3\2\2\2\u015e\u0160\t\b\2\2\u015f\u015e")
        buf.write("\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162l\3\2\2\2\u0163\u0161\3\2\2\2\u0164")
        buf.write("\u0168\t\t\2\2\u0165\u0167\t\4\2\2\u0166\u0165\3\2\2\2")
        buf.write("\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169\u0175\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c")
        buf.write("\7a\2\2\u016c\u0170\t\4\2\2\u016d\u016f\t\4\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3")
        buf.write("\2\2\2\u0173\u016b\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u017a\3\2\2\2\u0177")
        buf.write("\u0175\3\2\2\2\u0178\u017a\7\62\2\2\u0179\u0164\3\2\2")
        buf.write("\2\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c")
        buf.write("\b\67\3\2\u017cn\3\2\2\2\u017d\u017e\5m\67\2\u017e\u017f")
        buf.write("\5q9\2\u017f\u0188\3\2\2\2\u0180\u0181\5m\67\2\u0181\u0182")
        buf.write("\5q9\2\u0182\u0183\5s:\2\u0183\u0188\3\2\2\2\u0184\u0185")
        buf.write("\5m\67\2\u0185\u0186\5s:\2\u0186\u0188\3\2\2\2\u0187\u017d")
        buf.write("\3\2\2\2\u0187\u0180\3\2\2\2\u0187\u0184\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018a\b8\4\2\u018ap\3\2\2\2\u018b")
        buf.write("\u018c\7\60\2\2\u018c\u018d\5\t\5\2\u018dr\3\2\2\2\u018e")
        buf.write("\u018f\t\n\2\2\u018f\u0190\7-\2\2\u0190\u0197\5\t\5\2")
        buf.write("\u0191\u0192\t\n\2\2\u0192\u0193\7/\2\2\u0193\u0197\5")
        buf.write("\t\5\2\u0194\u0195\t\n\2\2\u0195\u0197\5\t\5\2\u0196\u018e")
        buf.write("\3\2\2\2\u0196\u0191\3\2\2\2\u0196\u0194\3\2\2\2\u0197")
        buf.write("t\3\2\2\2\u0198\u0199\7v\2\2\u0199\u019a\7t\2\2\u019a")
        buf.write("\u019b\7w\2\2\u019b\u01a2\7g\2\2\u019c\u019d\7h\2\2\u019d")
        buf.write("\u019e\7c\2\2\u019e\u019f\7n\2\2\u019f\u01a0\7u\2\2\u01a0")
        buf.write("\u01a2\7g\2\2\u01a1\u0198\3\2\2\2\u01a1\u019c\3\2\2\2")
        buf.write("\u01a2v\3\2\2\2\u01a3\u01a7\7$\2\2\u01a4\u01a6\5\13\6")
        buf.write("\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9")
        buf.write("\u01a7\3\2\2\2\u01aa\u01ab\7$\2\2\u01ab\u01ac\b<\5\2\u01ac")
        buf.write("x\3\2\2\2\u01ad\u01ae\13\2\2\2\u01ae\u01af\b=\6\2\u01af")
        buf.write("z\3\2\2\2\u01b0\u01b4\7$\2\2\u01b1\u01b3\5\13\6\2\u01b2")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6\u01b4\3")
        buf.write("\2\2\2\u01b7\u01b8\b>\7\2\u01b8|\3\2\2\2\u01b9\u01bd\7")
        buf.write("$\2\2\u01ba\u01bc\5\13\6\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be")
        buf.write("\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c1\5\17\b")
        buf.write("\2\u01c1\u01c2\b?\b\2\u01c2~\3\2\2\2\26\2\u0085\u0093")
        buf.write("\u009b\u00a2\u00a6\u00ae\u015c\u015f\u0161\u0168\u0170")
        buf.write("\u0175\u0179\u0187\u0196\u01a1\u01a7\u01b4\u01bd\t\b\2")
        buf.write("\2\3\67\2\38\3\3<\4\3=\5\3>\6\3?\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    LINE_COMMENT = 2
    WS = 3
    AUTO = 4
    BREAK = 5
    BOOL = 6
    DO = 7
    ELSE = 8
    FLOAT = 9
    FOR = 10
    FUNCT = 11
    IF = 12
    INT = 13
    RETURN = 14
    STR = 15
    WHILE = 16
    VOID = 17
    OUT = 18
    CONT = 19
    OF = 20
    INHER = 21
    ARR = 22
    ADD = 23
    MINUS = 24
    MUL = 25
    DIV = 26
    MOD = 27
    NOT = 28
    AND = 29
    OR = 30
    EQUAL = 31
    NEQ = 32
    SM = 33
    SMEQ = 34
    BG = 35
    BGEQ = 36
    STROP = 37
    LP = 38
    RP = 39
    LB = 40
    RB = 41
    LS = 42
    RS = 43
    EQ = 44
    COMMA = 45
    DOT = 46
    SEMI = 47
    COLON = 48
    ID = 49
    INTLIT = 50
    FLOATLIT = 51
    DECPART = 52
    EXPPART = 53
    BOOLIT = 54
    STRINGLIT = 55
    ERROR_CHAR = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "'='", "','", "'.'", 
            "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LINE_COMMENT", "WS", "AUTO", "BREAK", "BOOL", "DO", 
            "ELSE", "FLOAT", "FOR", "FUNCT", "IF", "INT", "RETURN", "STR", 
            "WHILE", "VOID", "OUT", "CONT", "OF", "INHER", "ARR", "ADD", 
            "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NEQ", 
            "SM", "SMEQ", "BG", "BGEQ", "STROP", "LP", "RP", "LB", "RB", 
            "LS", "RS", "EQ", "COMMA", "DOT", "SEMI", "COLON", "ID", "INTLIT", 
            "FLOATLIT", "DECPART", "EXPPART", "BOOLIT", "STRINGLIT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "LINE_COMMENT", "WS", "NUM", "CHAR", "ESC_SEQ", 
                  "ESC_ILL", "AUTO", "BREAK", "BOOL", "DO", "ELSE", "FLOAT", 
                  "FOR", "FUNCT", "IF", "INT", "RETURN", "STR", "WHILE", 
                  "VOID", "OUT", "CONT", "OF", "INHER", "ARR", "ADD", "MINUS", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NEQ", 
                  "SM", "SMEQ", "BG", "BGEQ", "STROP", "LP", "RP", "LB", 
                  "RB", "LS", "RS", "EQ", "COMMA", "DOT", "SEMI", "COLON", 
                  "ID", "INTLIT", "FLOATLIT", "DECPART", "EXPPART", "BOOLIT", 
                  "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[53] = self.INTLIT_action 
            actions[54] = self.FLOATLIT_action 
            actions[58] = self.STRINGLIT_action 
            actions[59] = self.ERROR_CHAR_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text.replace('"','',1))
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text.replace('"','',1))
     


