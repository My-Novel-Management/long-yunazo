# -*- coding: utf-8 -*-
'''
Stage: "stage name"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


def main_notes(w: World):
    return (
            )


# world settings
def world_note(w: World):
    return w.writer_note('世界設定',
            w.tag.title("基本的な世界観"),
            "魔力が普通のエネルギィ源として利用できるスチームパンク亜種な世界",
            "「魔素」を利用することで様々な機関を駆動させている",
            "それは蒸気や電気のような動力となり、中世欧州的世界を形成している",
            w.tag.title("武器"),
            "基本は剣術や槍術になるが、高価なものとして「魔銃」が存在している",
            "ただしそれはハンドガン程度のもので（後にライフルなども登場する）、一般人にはとても手が出せない代物である",
            w.tag.title("$enagy"),
            "$enagyは特殊な鉱石から抽出するのが一般的だが「魔導」を利用することでも手に入れられる",
            "魔導は$enagyをコントロールする術で、古文書にかかれている",
            "かつては人体から直接$enagyを操れた。そういう種族もいたし、訓練して使えるようになったものを「魔導師」などと呼んだ",
            "魔法使いもその亜種である",
            w.tag.title("$heroの存在"),
            "$heroと呼ばれる存在は既に伝説となり、それとともに$bossも古典になっている",
            "ただし$hero利権なるものが存在していて、その末裔は各王国や共和国で利権をむさぼっている",
            "一部$heroの末裔を名乗って義賊まがいの活動を行っている者もいる",
            w.tag.title("$monster"),
            "$monsterはかつて$bossが存在していた頃にその手先として活躍した闇の存在である",
            "動物が凶暴化したものが大半だが中には知性を持ち、人を騙したり、人になりかわったりする存在もいる",
            "実は$bossとはまた別の勢力で「闇の世界」と呼ばれる世界の住人と言われている",
            "今回のメイン敵はこの「闇の世界」の手先である",
            "$bossとはもともとその「闇の世界」の者の中である程度の力があるものが自分の国が欲しいとやってきた中から生まれたりしている",
            w.tag.title("現在の$boss"),
            "今の時点では$bossはいないと言われている",
            "世界は危険地域を除いてある程度平和に暮らしており、$bossの脅威にはさらされていない",
            "しかし数年に一度の周期で$bossの脅威と呼ばれる$monsterの大量発生がある",
            )


def calture_note(w: World):
    return w.writer_note("文化・技術について",
            w.tag.title("時間"),
            "ゼンマイは存在する",
            "$enagyを用いた開発技術があり、高額だが$enagy時計が存在する",
            "民衆はあまり正確な時計を使わず、時計台や時計塔と知らせの鐘で時間調整をする",
            w.tag.title("水道技術"),
            "あまり上質なものはない",
            "ただ汚くなりすぎてもあれなんで、簡易下水の技術は発達しているとする",
            )

