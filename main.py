from summa.summarizer import summarize

def summarizeArticle(article):
    return summarize(article)

def main():
    article = """Germany's domestic intelligence agency is to step up monitoring of the far-right Alternative for Germany (AfD) party for suspected extremism.

But the BfV agency is not yet going as far as to use informants or phone taps in its nationwide watch on AfD.

AfD is the main opposition party. It entered the federal parliament for the first time in 2017, winning 94 seats in the 709-seat lower house (Bundestag).

AfD sees Islam as a threat to German values, urging tough immigration curbs.

Just how far to the right is AfD?
The party is expected to do well in the European Parliament elections in May, like nationalists in many other EU countries.

The BfV will impose a higher level of surveillance on the AfD youth organisation JA and on an AfD grouping called Flügel (Wing).

Flügel is led by Björn Höcke, a controversial figure who drew sharp criticism when he labelled the Berlin Holocaust monument a "memorial of shame".

German far-right MP badly hurt in attack
Outcry at far-right child informer scheme
Anger over 'Nazis just bird poo' remark
The BfV has previously put a watch on some socialist politicians in Die Linke, a party with roots in the old East German Communist Party.

The BfV is empowered under the German constitution to act against perceived threats to the democratic order.

Some statements by AfD leaders have been condemned as encouraging neo-Nazi extremism. AfD activists took part in far-right rallies in the eastern city of Chemnitz last year, marred by clashes with police.

"""
    print(summarizeArticle(article))

if __name__ == "__main__":
    main()