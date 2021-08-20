import colorama
from colorama import Fore,Style,Back, init
RED = "> \x1b[1;31;40m"

def Neues_Spiel():
  print("Möchtest du noch einmal dem Drachen das Fürchten lehren? (J/N)")
  
  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "j" in answer:
    Vor_der_Schanze()
  else:
    print("DU BIST EINE SCHANDE FÜR DIE GANZE HAIDERSCHAFT, DU LVLNULLER!!!")

def game_over(reason):
  print("\n" + reason)
  print("\n")
  print("GAME OVER!")
  print("\n")
  Neues_Spiel()

def Vor_der_Schanze():
  print("""Hier bist du also. An der berüchtigsten Schanze Meddlfrankens. Unter der Woche und vor 17 Uhr. 
  Warum? Weil du ein arbeitsloser Student bist und eh nichts besseres zu tun hast.Viel zu lange schon wolltest 
  du dir das Elend am Alschauerberg 8 in 91448 Emskirchen einmal selbst anschauen. Die Wut, die der Butterschmalzoger
  in dir die letzten Jahre über ausgelöst hat, willst du endlich loswerden. Du willst dem Treiben ein Ende setzen. 
  Du willst Rudis Erbe erfüllen. Du willst dem Drachen das Fürchten lehren. Du willst hergehen und Scheiße bauen. 
  Besser noch: Du willst die legendären Rudi Tapes finden und sie der Welt dort draußen zur Verfügung stellen. Du weißt, 
  dass sie so brisant sind, dass sie das Game beenden können. Dein ganzes Lebne hast du dich für diesen einen Tag vorbereitet.
  Ja, du bist es:
  
  DU BIST DERJENICHE!

  Du steigst aus deinem 1997er Toyota Corolla, schließt mit einem Ruck die Tür hinter dir und atmest noch
  einmal durch. Vor die steht ein baufälliges, heruntergekommenes Anwesen. Die Fassade erstrahlt längst nicht mehr
  in dem strahlenden Gelb, wie es vielleicht mal vor 20 Jahren war. Stattdessen zieren zerschlagene Eier die Hauswand
  und an manchen Stellen wurde der Putz von einem Hochdruckreiniger weggefegt. Du fragst dich, wer so dumm sein kann, 
  dass er denkt, mit einem HOCHDRUCKWASSERREINIGER seine Hauswand zu säubern. Dann fällt dir wieder ein,
  wo du dich gerade befindest. Du trittst näher an das metallische Hoftor heran, das von den letzten dreihundert Besuchen 
  ziemlich in Mitleidenschaft gezogen wurde. Als du einen Fuß auf das Grundstügg von Häutpling Wasserbein setzt, ertönt 
  das charakteristische "Wiwiwiwiwi Wiwiwiwiwi". Du weißt nicht, ob der Speckbeppo dich schon bemerkt hat oder nicht. 
  Du möchtest lieber unerkannt bleiben. Schließlich möchtest du in die Schanze eindringen um die Rudi-Tapes zu bergen. 
  Was machst du?
  
  1. Handy rausholen und hochkant filmen.
  2. "Herr Winklaaa, kommen Sie heraus und betreibne Sie Fanmanagement" brüllen, um den Oger abzulenkne.
  3. Deinen Mut zusammenehmen, dem Risiko ins Auge sehen und volles Mett über das Geländer klettern. """)
  
  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("\n")
    game_over("Sammal, hast du se noch alle??? Wie oft soll man dir noch sagne, dass man nicht hochkant filmne soll?! Lösch dich!")
  elif "2" in answer:
    print("""Als du 5min lang erfolglos gen Schanze brüllst, kommt auf einmal eine Streife hergefahren. Ein Beamter 
    mittleren Alters steigt aus und kommt mit genervten Blick auf dich zu. Er stellt sich als "Herrn Müller der PINEA" 
    vor und fragt, was du hier machst. Was sagst du?
   
    1. Du bist hier, weil du dem Reiner volles Pfund aufs Maul gebne willst.
    2. Du möchtest die Bürger Altschauerbergs endlich von ihrem Leid erlösen und das Drachengame beenden.
    3. Du sagst nichts, sondern blickst Herrn Müller wortlos in die Augen. Alles ist bereits gesagt. """)
    
    answer = input(RED).lower()
    print(Style.RESET_ALL)
    
    if "1" in answer:
      print("\n")
      game_over("""Herr Müller kann nicht anders und erteilt dir einen Platzverweis. An seinem Blick erkennst du, dass er es nicht gerne tut. 
      Überleg das nächste Mal, was du einem Polizeibeamten erzählst.""")
    elif "2" in answer:
      print("""Herr Müller stockt und weicht zurück. Er erkennt deine Bestimmung. Er erkennt, dass du DERJENICHE bist, der hergeht. Er lässt dich walten.
      Du nickst ihm zu und kletterst über das kaputte Hoftor.""")
      print("\n")
      Hof()
    elif "3" in answer:
      print("""Eure Blicke vereinigen sich zu einer stummen Bruderschaft. Er weiß es, du weißt es. Du bist DERJENICHE. Herr Müller nickt dir zu und lässt dich walten.
      Du gehst auf Bumsdis Grundstügg und kletterst über kaputten Zaun.""")
      print("\n")
      Hof()
    else:
      print("Gib das ein, was da steht, du Kaggnazi!")
      print("\n")
      Vor_der_Schanze()
  elif "3" in answer:
    print("Du klettert an der linken Seite zwischen Hoftor und ehemaliger Scheune hindurch. Noch hat Reiner dich nicht bemerkt.")
    print("\n")
    Hof()
  else:
    print("Wie wärs mal, wenn du dich fapisst, wenn du nicht das Richtige eingebne willst?!")
    print("\n")
    Vor_der_Schanze()

def Hof():
  print("""Hier stehst du also. Mitten auf dem zugemüllten Grundstügg Bumsdis. Überall Unrat, Autoreifen, Eierschalen und...was ist das dort hinten?
  Eine Wurst?! Egal. Du schaust dich weiter um. Du hast jetzt die Wahl. Gehst du geradeaus, Richtung zukünftige Methalle und suchst dort nach den Tapes? 
  Oder wagst du dich direkt in die Höhle des Ogers?
  
  1. Du gehst in die Met(t)halle.
  2. Du gehst in die Schimmelburg.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("""Du bewegst dich vorbei am rudi-roten Audi, der wo nicht fährt und trittst durch die mächtigen Scheunentore, der zugegebenermaßen,
    völlig verlotterten Garagenhalle.""")
    print("\n")
    Methalle()
  elif "2" in answer:
    print("""Du bewegst dich zur Eingangstür. Bis du dorthin kommst, musst du dich durch kaputte Möbel und noch mehr Unrat kämpfen. 
    Hier wurden viele Schlachten geschlagen. Aber auch schöne Erinnerungen gehen dir durch den Kopf. Die Zeit des Bosterverkaufs, zum Beispiel.
    Doch es ist keine Zeit für Sentimentalitäten. Du bist wegen etwas anderen hier. Du nimmst die wenigen Stufen rauf zur Eingangstür. 
    Ab jetzt zählt jede Sekunde. Reiner hat dich noch nicht bemerkt, was höchst ungewöhnlich ist. Schläft er noch? Macht er ph Videos? 
    Egal, du bist hier und er nicht. Damit hast du mehr erreicht, als dutzende Haider zuvor. Du betätigst die Türklinke. Aber oh nein! Sie klemmt! 
    Was tust du?
    
    1. Du reißst an der Klinke herum, mit der Hoffnung, dass die Tür sich öffnet.
    2. Du drückst die Klingel(ständer) und wartest ab, was passiert.
    3. Du schaust dich weiter um.""")
  
    answer = input(RED).lower()
    print(Style.RESET_ALL)
    if "1" in answer:
      print("""Es passiert nichts. Die Tür lässt sich nicht aufmeddln. Jetzt behalte bloß die Nerven!
      
      1. Ruhig durchatmen, an Reiners letztes einstündiges "Laber" Video denkne und es noch einmal versuchen.
      2. An Reiners Einnahmen der letzten Monate denkne und durchdrehne.""")
    
      answer = input(RED).lower()
      print(Style.RESET_ALL)
      if "1" in answer:
        print("Die Tür lässt sich öffnen.")
        print("\n")
        Hausflur()
      elif "2" in answer:
        print("\n")
        game_over("Du hattest nur eine Aufgabe. Ruhig bleibne! Wahrscheinlich hast du dem Diggn auch noch Klicks geschenkt. Lösch dich!")
      else: 
        print("Verdammte Wiggsgrübbl. Gib halt das Richtige ein!")
        print("\n")
        Hof()
    elif "2" in answer:
      print("\n")
      game_over("""Du hörst, wie es in der Schanze anfängt zu donnern. Du spürst die Vibrationen. Die Einschläge kommen näher.
      Auf einmal geht die Tür auf und ein stinkendes Ungetier, knapp 1,89 groß, stellt sich dir schnaubend entgegne. Rainer erkennt dich
      als Haider und brüllheult: "RUNNA VON MEIM GRUNDSTÜGG SONST ZERHAGG ICH DICH IN KLEINE STÜGGE DU HURESOOOOOHN! Du flüchtest.""")
    elif "3" in answer:
      print("""Du schaust dich um. Aber außer Müll, einer blauen Tonne und einem Strauch neben dem Haus, kannst du nichts sehen. Was tust du?
      
      1. Zur blauen Tonne gehen.
      2. Zum Strauch neben dem Haus gehen.""")

      answer = input(RED).lower()
      print(Style.RESET_ALL)
      if "1" in answer:
        print("""Du trittst an die blaue Tonne heran. Ein widerwärtiger Geruch steigt aus ihr heraus. Jeder Schritt näher an die Tonne, 
        lässt den Gestank intensivieren. Willst du wirklich näher an diese Tone rangehen?? (J/N)""")
  
        answer = input(RED).lower()
        print(Style.RESET_ALL)
        if "j" in answer:
          print("\n")
          game_over("""Du musst fast würgen, als du an die Tonne herantrittst. Du schaust hinein, doch weichst sofort zurück, völlig aufgelöst. 
          Die Gerüchte stimmen. Oh mein Gott, die Gerüchte sind alle wahr. In der blauen Tonne liegt eine verrottende Ente. Du musst würgen.
          Das hast du nicht erwartet. Wie widerwärtig. Wie schlimm ist es dann erst im Haus??? Du flüchtest wieder.""")
        elif "n" in answer:
          print("Gute Entscheidung. Du gehst zurück zur Tür und versuchst es noch einmal. Diesmal lässt sie sich öffnen.")
          print("\n")
          Hausflur()
        else:
          print("Figg dich, du unfähiges Stügg.")
          print("\n")
          Hof()
      elif "2" in answer:
        print("""Du durchsuchst den Strauch. Du findest eine kleine, rote, aber auffällig gold leuchtende Frucht. Ist das wirklich eine...
        ist das wirklich eine HAGEBUDDNE??? Du zupfst sie vorsichtig vom Busch und nimmst sie in den Mund. Sofort fühlst du dich von einer 
        Grieselkrätze geheilt, die du niemals hattest und bist nun motiviert denn je, die Rudi-Tapes zu finden. Du gehst einfach zur Tür und öffnest sie.""")
        print("\n")
        Hausflur()
      else:
        print("Maaaaan, gib halt das richtige ein!!!")
        print("\n")
        Hof()
  else:
    print("Schon wieder die falsche Wahl getroffne. Lösch dich doch einfach.")
    print("\n")
    Hof()
  
def Methalle():
  print("""Ein Geruch von alten Reifen und Öl steigt dir in die Nase. Es ist hier so viel Müll, dass du nicht weißt, wo du anfangen sollst zu suchen.
  Du siehst eine Werkbank und eine kleine Treppe in ein Obergeschoss, aber auch auf dem Boden liegt sehr viel Zeug. Was tust du?
  
  1. Du durchsuchst die Werkbank.
  2. Du nimmst die Treppe.
  3. Du schaust dich weiter auf dem Boden um.
  4. Du gehst zurück in den Hof.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("""Jede Menge unaufgeräumtes Werkzeug liegt auf der Bank. Hier und da ein klebriges Taschentuch und eine halbvolle Monster-Energy Dose.
    Keine Spur von den Rudi-Tapes. Du schaust dich weiter um.""")
    print("\n")
    Methalle()

  elif "2" in answer:
    print("Die Treppe sieht gefährlich morsch aus. Willst du es wirklich wagen, da hochzugehen? (J/N)")
    
    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "j" in answer:
      print("\n")
      game_over("Glaubst du wirklich, Reiner hätte die Rudi-Tapes nicht gut versteckt? Und glaubst du ERNSTHAFT, Reiner hätte sie da oben versteckt? Lösch dich!")
    elif "n" in answer:
      print("Gute Entscheidung. Rudis Bua hätte sich nie dort hoch getraut. Du gehst zurück.")
      print("\n")
      Methalle()
    else:
      print("TIPP. WAS. RICHTIGES. NEI. !!!")
      print("\n")
      Methalle()

  elif "3" in answer:
    print("""Du schaust dich um, wühlst dich durch den Dreck, watest durch Müll, den garantiert nur ein Messi hinterlassen kann. Aber du findest nichts.
    Nichts, außer der Gewissheit, dass diese Halle niemals zum Met trinken gebraucht werden wird. Nein, vorher wird sie zusammenfallen, wie auch der Rest
    von Rudis Erbe. Dir entgleitet eine Träne. Du gehst zurück.""")
    print("\n")
    Methalle()

  elif "4" in answer:
    Hof()  
  else:
    print("Bidde ferlass uns.")
    print("\n")
    Methalle()

def Hausflur():
  print("""Du hast es geschafft. Du befindest dich in den heiligen Hallen. Auf der rechten Seite siehst du die Treppe, die nach oben führt.
  Links geht es in den sagenumwobenen Radelraum und geradeaus hindurch geht es zur Küche, dem Badezimmer und natürlich der Wohnarbeitsspielküche. 
  Als du so nach vorne blickst, musst du an das erste Video des Drechen denkne. Das Tanzfideo. Damals war er noch dünn. Das war vor der 250kg Staffel. 
  Schöne Zeiten. Wohin möchtest du als erstes gehen?
  
  1. Gehe ins Obergeschoss.
  2. Gehe in den Radelraum.
  3. Gehe in die Küche.
  4. Gehe ins Badezimmer.
  5. Gehe in die Streamzimmer.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    Obergeschoss()
  elif "2" in answer:
    Radelraum()
  elif "3" in answer:
    Küche()
  elif "4" in answer:
    Badezimmer_1()
  elif "5" in answer:
    Streamzimmer()
  else:
    print("Ich schmaß dir so die Brügl naus!")
    print("\n")
    Hausflur()

def Radelraum():
  print("""Du findest dich in einem zugemüllten Raum wieder. Die Decke ist mit hässlichen Graffitis beschmiert, genauso wie die Wände.
  Es riecht nach abgestandenen Urin. Du erkennst mehere unbenutzte Sportgeräte sowie einen kaputten Hometrainer. Du erinnerst dich
  an die lustigen Videos, als Reiner noch abnehmen wollte, haha. Egal, du schaust dich um, aber nichts lässt darauf schließen, dass 
  hier irgendwo die Rudi-Tapes versteckt sein könnten. Was tust du?
  
  1. Du gehst weiter zur Küche.
  2. Du gehst zurück zum Flur und ins Streamzimmer.
  3. Du gehst wieder zurück in den Flur. """)
  
  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("Du watest durch den Müll und öffnest die Tür zur Küche. Eigentlich schiebst du aber nur ein Brett an der Wand zur Seite.")
    print("\n")
    Küche()
  elif "2" in answer:
    Streamzimmer()
  elif "3" in answer:
    Hausflur()
  else:
    print("Haaaaauuuuuu aaaaaaaaaab!")
    print("\n")
    Radelraum()

def Küche():
  print("""Ein ekelhafter Gestank macht sich breit. Du weißt, du bist in der Küche. Wobei man diesen Ort nicht mehr Küche nennen kann.
  Hier und da bewegt sich etwas zwischen den Töpfen und Tellern. Wahrscheinlich sind es die Kakerlaken, die ein paar Ehrenmänner
  einmal vor Jahren in die Schanze hineingeschmuggelt haben. Vielleicht sind es aber auch Mäuse. Es ist dir egal. Du weißt nur,
  dass hier ein normaler Mensch nichts kochen könnte. Aber Rainer ist halt ein ganz besonderer Mensch. Und mit besonders meine ich...
  Die einzige Möglichkeit, wo hier die Rudi-Tapes versteckt sein könnten, ist ein geschlossener Schrank in der Ecke der Küche.
  Oder im Kühlschrank selbst. Das wäre zwar sehr dumm. Aber du unterschätzt des immer, wie dumm der Reiner eigentlich ist. Was tust du?
  
  1. Du öffnest den geschlossenen Schrank.
  2. Du schaust in den Kühlschrank.
  3. Du machst spontan ein "Projekt Brötchen", weil du Hunger bekommst.
  4. Du gehst zurück zum Radelraum.
  5. Du gehst durch den Flur ins Streamzimmer.
  6. Du gehst zurück in den Flur.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("""Ein paar Tassen, Pfannen und weiterer Unrat (so viel Unrat...) türmt sich in dem Schrank. Du wühlst dich hindurch. Aber du findest
    rein gar nichts. Enttäuschend.""")
    print("\n")
    Küche()
  elif "2" in answer:
    print("""Mozarellakugeln, Lyoner und etliche andere JA- Produkte türmen sich in dem viel zu kleinen, seit Ewigkeiten nicht mehr geputzen Kühlschrank. 
    Es stinkt. Aber das hält dich nicht davon ab, weiter diesen ekelhaften Kühlschrank zu durchwühlen. Du entdeckst ein in Zeitungspapier umhülltes Etwas.
    Was tust du?
    
    1. Du holst es heraus und schaust es dir genauer an.
    2. Du lässt es dort liegen.""")
    
    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "1" in answer:
      print("""Du nimmst das Etwas in deine Hand und packst es langsam aus. Es ist eine alte Butterdose mit der Aufschrift 'Kriokammmer'. 
      Was tust du?
      
      1. Die Dose öffnen.
      2. Die Dose wieder zurücklegne.""")

      answer = input(RED).lower()
      print(Style.RESET_ALL)

      if "1" in answer:
        print("""Du öffnest die Dose langsam. Was du darin findest, lässt dich erschaudern. Es ist ein skelettierter Überrest von Etwas,
        das einmal ein Hamster hätte sein können. Du bist angewidert, wirfst die Dose in die Egge und rennst zum Badezimmer, da du das Gefühl hast,
        dich übergeben zu müssen.""")
        print("\n")
        Badezimmer_1()
      elif "2" in answer:
        print("Wahrscheinlich die bessere Entscheidung. Du legst die Dose zurück und schaust dich wieder in der Küche um.")
        print("\n")
        Küche()
      else:
        print("Halt your mouth and go delete you.")
        print("\n")
        Küche()
    elif "2" in answer:
      print("Wahrscheinlich die bessere Entscheidung. Du lässt das Etwas im Kühlschrank und schaust dich wieder in der Küche um.")
      print("\n")
      Küche()
    else:
      print("Ich hab hier die Macht. Und jetzt fapiss dich, wenn du dich nicht an die Regeln hälst!")
      print("\n")
      Küche()
  elif "3" in answer:
    print("\n")
    game_over("Du bist nicht du, wenn du hungrig bist. Aber das ist nun wirklich danebne. Dein Ziel sind die Rudi-Tapes, du lvl Nuller!")
  elif "4" in answer:
    print("Du läufst zurück zum Radelraum.")
    print("\n")
    Radelraum()
  elif "5" in answer:
    print("Du läufst weiter zum Streamzimmer.")
    print("\n")
    Streamzimmer()
  elif "6" in answer:
    print("\n")
    Hausflur()
  else:
    print("Kein Bock mehr auf den Scheißdreck.")
    print("\n")
    Küche()

def Badezimmer_1():
  print("""Du erschauderst, als du die Tür zum Badezimmer öffnest. Du hast die Bilder im Internetz gesehen, aber die Realität ist dann doch nochmal krasser. 
  Nicht nur Geruch von Urin und Kot setzt sich in deine Nase, nein, auch einen modrigen, etwas urigen Geruch kannst du herausfiltern. 
  Wohin "möchtest" du als erstes in dieser sanitären Hölle gehen?
  
  1. Zur Dusche.
  2. Zum Waschbecken.
  3. Zur Toilette.
  4. Zurück zur Küche.
  5. Zurück zum Radelraum.
  6. Zurück zum Streamingzimmer.
  7. Bloß raus hier!""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("""KAGGDUSCHNE! Das ist das erste Wort, das dir einfällt, bei diesem Anblick einer heruntergekommenen Version
    einer Dusche. Auf dem Duschboden finden sich ekelerregende braune Spuren. Als du die Duschwand etwas genauer betrachtest,
    kommt sie dir irgendwie bekannt vor. Willst du weiter darüber nachdenken? (J/N)""")

    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "j" in answer:
      print("Bist du dir sicher? (J/N)")

      answer = input(RED).lower()
      print(Style.RESET_ALL)

      if "j" in answer:
        print("\n")
        game_over("""Du überlegst und überlegst. Auf einmal kommt es dir wie ein Blitz ins Gehirn geschossne! Du weißt,
        woher du diese Dusche kennst. Aber du hast es die ganze Zeit über verdrängt gehabt. Doch jetzt steigen dir diese grauen-
        vollen Bilder wieder in den Kopf und du siehst vor deinem inneren Auge, wie sich Rainer und der schwarze Luan in dieser
        Dusche miteinander verbinden. Das wars, das hält kein normaler Mensch aus. Scheiß auf die Rudi-Tapes! Deine Gesundheit ist
        dir wichtiger. Du flüchtest.""")
      elif "n" in answer:
        print("Du denkst nicht weiter darüber nach. Wird schon nichts wichtiges gewesen sein. Du findest nichts weiter spannendes.")
        print("\n")
        Badezimmer_1()
      else:
        print("Du weißt selbst warummäh oder?!")
        print("\n")
        Badezimmer_1()

    elif "n" in answer:
      print("Du denkst nicht weiter darüber nach. Wird schon nichts wichtiges gewesen sein. Du findest nichts weiter spannendes.")
      print("\n")
      Badezimmer_1()
    else:
      print("Du denkst auch nur an das eine oder? Lösch dich.")
      print("\n")
      Badezimmer_1()

  elif "2" in answer:
    print("""Du schaust dir das Waschbecken genauer an. Du siehst, natürlich, mehrere "Sodild" auf dem Rand stehen. Aber auch seltsame
    Dinge, wie Schminkzeug und eine Bastelschere. Aber sonst nichts weiter spannendes.""")
    print("\n")
    Badezimmer_1()
  elif "3" in answer:
    print("Was erwartest du? Es ist eine Toilette, in die ein übergewichtiger, unhygienischer Oger uriniert. Genau so sieht sie aus.")
    print("\n")
    Badezimmer_1()
  elif "4" in answer:
    print("Du gehst zur Küche.")
    print("\n")
    Küche()
  elif "5" in answer:
    print("Du gehst zum Radelraum.")
    print("\n")
    Radelraum()
  elif "6" in answer:
    print("Du gehst ins Streamingzimmer.")
    print("\n")
    Streamzimmer()
  elif "7" in answer:
    Hausflur()
  else: 
    print("Ja, es ist eklig. Aber versuch trotzdem das nächste Mal, das richtige einzugebne.")
    print("\n")
    Badezimmer_1()

def Streamzimmer():
  print("""Du betrittst das Streamzimmer. Ein vergilbter Greenscream und verlotterte Softboxne zieren einen kleinen Stuhl.
  Ansonsten ist das Zimmer leer. Der selbe Dreck wie überall, aber sonst ist es überraschend uninteressant. Wahrscheinlich
  soll es nur die Vorhölle darstellen, bevor du zur Wohnarbeitsspielküche kommst. Wenn dort die Rudi-Tapes nicht sind, dann weißt du auch nicht.
  
  1. Zur Wohnarbeitsspielküche weitergehne.
  2. Zurück zum Flur gehne.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("Ein vielversprechender Raum. Du betrittst die Wohnarbeitsspielküche.")
    print("\n")
    Wohnarbeitsspielküche()
  elif "2" in answer:
    print("Du gehst zurück zum Flur.")
    print("\n")
    Hausflur()
  else:
    print("Gib a Ruh!")
    print("\n")
    Streamzimmer()

def Wohnarbeitsspielküche():
  print("""Was für ein Anblick. Du weißt gar nicht, wo du zuerst hinschauen sollst. Überall steht, liegt oder fault etwas. An den
  widerwärtigen Geruch hast du dich längst gewöhnt. Du hast nur noch einen Blick für all die Dinge, die du in den unzähligen Screams
  immer wieder einmal gesehen hast. Und es ist alles so, wie du es dir vorgestellt hast. Es ist eklig. Es ist unhygienisch. Es ist typisch
  Reiner. Meddl! Was möchtest du dir als erstes anschauen?
  
  1. Das Zarensofa.
  2. Den Schreibtisch des Lords.
  3. Den Bereich hinter dem Gamingchair bei der Spüle.
  4. Den Rest des Zimmers.
  5. Du möchtest die andere Räume sehen.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("""Das grüne Zarensofa. Wie es leibt und lebt. Wahrscheinlich schon mehr als 60 Jahre alt, hat es schon so viel erlebt
    und erleben müssen. Welches Sofa erträgt schon so lange einen Winklaaa auf sich, ohne irgendwann nachzugebne. Ja, dieses Sofa 
    hat ausgedient. Man kann deutlich eine Kuhle erkennen. Ja, die Flecken überall erzählen auch vom Leid dieses Sofas. Es hat viel
    gesehen. 
    
    1. Dir das Sofa genauer anschauen.
    2. Dich vom Sofa abwendne.""")

    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "1" in answer:
      print("""Du nimmst deinen Mut zusammen und greifst mit deiner bloßen Hand in die Ritzen des Sofas. Es ist klebrig. Du drückst deine
      Hand tief in die Polster, in der Hoffnung irgendetwas zu findne. Aber außer vieler Krümel in den verschiedensten Farben und
      Konsistenzen, kannst du leider nichts findne.""")
      print("\n")
      Wohnarbeitsspielküche()
    elif "2" in answer:
      Wohnarbeitsspielküche()
    
    else:
      print("GIB DOCH DIE RICHTIGE ZAHL EIN!")
      print("\n")
      Wohnarbeitsspielküche()

  elif "2" in answer:
    print("""Die offizielle Kommandozentrale. Hier spielt sich üblicherweise alles ab. Hier wird, gebrüllheult, gestreamt, gegessne,
    getrunkne, geschriene, gespielt und natürlich auch viel gew*****. Hier wird Alexa gequält und die Drachis auch. In der Realität und
    ohne Reiner (wo steckt er überhaupt???) sieht dieser Ort aber wesentlich karger und trauriger aus, als du ihn kennst. In Wirklichkeit
    ist das hier nichts anderes, als eine messihafte Bruchbude, in der es schimmelt und stinkt. Kein Mensch kann hier glücklich werdne oder
    sich auch nur eine Sekunde lang wohlfühlne. Du fragst dich, wie es Kevin Wolter solange da drin ausgehalten hat. Aber dann fällt dir ein, dass
    Kevin Wolter ein A-Loch ist und A-Löcher keine Ehre besitzen. Beantwortet das deine Frage? Nein, aber es ist eben ein Statement.
    Du schaust dich um. Aber du findest nichts interessantes. Alles was du unter all dem Dreck und Müll findest, ist belanglos. Doch
    dann findest du plötzlich einen auffällig abgenutzten Knopf, direkt neben dem Bildschim, auf dem normalerweise die Ansicht der Video-
    kameras zu finden ist. Möchtest du ihn drücken? (J/N)""")

    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "j" in answer:
      print("von draußen hörst du ein lautes 'wiwiwiwiwi wiwiwiwiwi' Du lächelst sanft und schaust dich weiter um.")
      print("\n")
      Wohnarbeitsspielküche()
    elif "n" in answer:
      print("Du schaust dich weiter um.")
      print("\n")
      Wohnarbeitsspielküche()
    else:
      print("Ezio, du bist ein verdammter Vollidiot!")
      print("\n")
      Wohnarbeitsspielküche()

  elif "3" in answer:
    print("""Es türmen sich die Ja-Verpackungen, Monster Dosen und Klopapierfetzen. Auf der Spüle hinter dem mittlerweile schon stark in
    Mitleidenschaft gezogenen Gaming-Chair, findet sich eine fast leere Packung Würfelzucker, eine Dose Instant-Kaffee und eine Schachtel Zigaretten.
    Du möchtest nicht weiter durch den Müll wühlen. Aber deine Hände sauber machen vielleicht machen schon. Was tust du?
    
    1. Die Spüle benutzen.
    2. Dir ein Tuch vom Boden aufheben und dich damit säubern.
    3. Nichts davon. Du schaust dich weiter um.""")
    
    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "1" in answer:
      print("Ein ekelhafter Strahl aus braunen und gelben Wasser schießt durch die Leitung der Spüle. Nein danke. Du gehst zurück.")
      print("\n")
      Wohnarbeitsspielküche()
    elif "2" in answer:
      game_over("Wie ekelhaft bist du eigentlich? Lösch dich, du Schmutz!")
    elif "3" in answer:
      Wohnarbeitsspielküche()
    else:
      print("Da, da isser scho wieder! Lösch diiiiich!")
      print("\n")
      Wohnarbeitsspielküche()

  elif "4" in answer:
    print("""So sehr du es auch versuchst, du findest nichts interessantes. Die Rudi Tapes sind nicht hier.
    Aber du siehst einen sehr kleinen Safe. Er verlangt von dir einen 15-stelligen Code. Was tust du:
    
    1. Code eingebne.
    2. Weiter die Wohnarbeitsspielküche durchsuchen.
    3. Zum Flur zurück gehne.""")

    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "1" in answer:
      print("Du gibst den Code ein:")
      answer = input(RED).lower()
      print(Style.RESET_ALL)

      if "drachenlord1510" in answer:
        print("\n")
        Easteregg()
      else: 
        print("Das ist nicht der richtige Code!")
        print("\n")
        Wohnarbeitsspielküche()

    elif "2" in answer:
      print("Du schaust dich weiter um.")
      print("\n")
      Wohnarbeitsspielküche()
    elif "3" in answer:
      print("Du gehst zurück zum Flur.")
      print("\n")
      Hausflur()
    else:
      print("Jesus Christ und Odin! Lösch dich!")
      print("\n")
      Wohnarbeitsspielküche()

  elif "5" in answer:
    print("Du gehst zurück zum Flur.")
    print("\n")
    Hausflur()
  else:
    print("Achte bidde auf deine Rechschreibung!")
    print("\n")
    Wohnarbeitsspielküche()
  
def Obergeschoss():
  print("""Der Gestank wird immer unerträglicher. Und du machst dir langsam Sorgne. Wo ist Reiner? Du hörst nichts,
  außer das leise Knabbern der Ratten im Gemäuer. Du bist nun im Obergeschoss. Vor dir liegt das zweite Badezimmer.
  Rechts geht es zum alten Streamzimmer und zum Schlafzimmer. Links geht es zu Ramonas alten Zimmer. 
  Wohin möchtest du gehne?
  
  1. Badezimmer.
  2. Altes Streamzimmer.
  3. Ramonas altes Zimmer.
  4. Wieder runter ins Erdgeschoss.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("Du bewegst dich leise ins Badezimmer.")
    print("\n")
    Badezimmer_2()
  elif "2" in answer:
    print("Du machst dich leise auf zum alten Streamzimmer.")
    print("\n")
    Altes_Streamzimmer()
  elif "3" in answer:
    print("Du gehst in Ramonas altes Zimmer.")
    print("\n")
    Hamsterzimmer()
  elif "4" in answer:
    print("Du gehst die Treppen wieder runter.")
    print("\n")
    Hausflur()
  else:
    print("Mach dich weg oder gib was richtiges ein!")
    print("\n")
    Obergeschoss()

def Badezimmer_2():
  print("""Du stehst nun im oberen Badezimmer. Die braunen Kacheln am Boden werden von schwarzen,
  versifften Rändern umrahmt. Auch hier liegt wieder überall Dreck und Unrat. Die grünen Amaturen
  vervollständigen den Look dieses, in die Tage gekommene Badezimmers. Was möchtest du tun?

  1. Dich umschauen.
  2. In den Spiegel schauen.
  3. Zurück in den Flur gehen.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer: 
    print("""Du möchtest in die Badewanne schauen, als du plötzlich über etwas glitschiges ruschst 
    und den Halt verlierst. Was tust du?

    1. Du lässt dich fallen. So schlimm kann es auf dem Boden nicht sein.
    2. Du versuchst dich am Waschbecken festzuhalten.
    3. Du sagst die magischen Worte um deine Haltung wiederzuerlangen. (Wer bleibt unbesiegt?)""")

    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "1" in answer:
      print("\n")
      game_over("""Als du fällst, knallst du mit dem Kopf gegen die versiffte Toilette. Benommen und
      blutend, siehst du, auf was du ausgerutscht bist. Es ist ein volles Kondom des Lards. Als du langsam
      dahinsiechst, kommt dir dein Frühstück wieder hoch, RIP""")
    elif "2" in answer:
      print("""Du hast es geschafft. Allerdings siehst du, dass du über ein benutztes Kondom gerutscht bist.
      Du ringst um Fassung, aber kannst gerade noch das Frühstück in dir halten. Du beschließt, das Bade-
      zimmer wieder zu verlassen.""")
      print("\n")
      Obergeschoss()
    elif "ich bleibe unbesiegt" in answer:
      print("""Sofort fühlst du dich stärker. Als ob dir all das Leid nichts antun kann. Du schaust auf den
      Boden und siehst ein benutztes Kondom. Aber das kann dir nichts anhaben. Du bist unbesiegt. Du weißt
      auf einmal intuitiv, wo die Rudi-Tapes versteckt liegen. Du weißt, dass sie in einem Safe unter Ruiners
      Bett sind. Du kennst die Kombination für den Safe. Jeder kennt die Kombination für den Safe. Du bist es,
      du bist DERJENICHE und hast deine Rolle jetzt entgültig akzebbdiert. Meddl. Du gehst zurück in den Flur.""")
      print("\n")
      Obergeschoss()
    else:
      print("Mach mal deinen Dschobb richtich.")
      print("\n")
      Badezimmer_2()
  
  elif "2" in answer:
    print("""Als du in den Spiegel schaust und kaum dein eigenes Gesicht auf der fettverschmierten Oberfläche erkennst
    kommt dir eine seltsame Idee. Du sagst intutiv viermal hintereinander "Rudi" in den Spiegel. Komm, traust
    du dich es ein fünftes Mal zu sagne? (J/N)""")

    answer = input(RED).lower()
    print(Style.RESET_ALL)
    
    if "j" in answer:
      print("\n")
      game_over("""Als du fünfmal hintereinander Rudi in den Spiegel sagst, siehst du, wie hinter dir die Kontur einer
      imposanten Gestalt auftaucht. Es ist Rudi, der von den Toten auferstanden ist. In der Hand hält er die goldene
      Luger. Doch es ist Zombie-Rudi. Er hebt seinen rechten Arm zum Gruß und schießt 1510 mal auf dich. RIP.""")
    elif "n" in answer:
      print("Wahrscheinlich die bessere Wahl.")
      print("\n")
      Badezimmer_2()  
    else:
      print("Ezio! Eziooooooo!")
      print("\n")
      Badezimmer_2()

  elif "3" in answer:
    Obergeschoss()
  else:
    print("Mach doch einmal das, was du machne sollst, verdammte Aggst.")
    print("\n")
    Badezimmer_2()

def Hamsterzimmer():
  print("""Als du dich zum alten Zimmer von Ramoner bewegst, fällt dir das große Loch an der Tür auf.
  Du erinnerst dich, wie Rainer bei seiner ersten Roomtour mit Piraten-Johnny erzählte, dass er einmal mit seiner 
  Schwester Streit hatte und vor lauter Wut, ein Loch in die Tür geschlagne hat. Rainer hatte wohl schon immer 
  Aggressionsprobleme.  Als du im Zimmer stehst, siehst du (neben Müll) nur den alten Hamster-Käfig. Was tust du?
  
  1. Du schaust dir den Hamsterkäfig genauer an.
  2. Du schaust dich im Zimmer um.
  3. Du gehst wieder zurück in den Flur.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("""Der Käfig sieht so aus, als wäre er seit Jahren nicht mehr berührt worden. Das Streu fängt langsam 
    an zu lebne und das Gitter setzt Rost an. Du kannst den Käfig öffnen, wenn du willst. (J/N)""")

    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "j" in answer:
      print("""Als du den Käfig öffnest und die zweite Ebene entfernst, findest du ein kleines Häuschen. Als
      du es anhebst, entblößt du darunter die Überreste von etwas, das einmal ein Hamster hätte sein können.
      Armes Ding, du wusstest es schon immer, dass Hamster keinen Winterschlaf machen. Du verdrückst eine Träne und schaust dich
      im Zimmer weiter um.""")
      print("\n")
      Hamsterzimmer()
    elif "n" in answer:
      print("Wir wissen alle, was sich in diesem Käfig befindet. Von wegen Winterschlaf...")
      print("\n")
      Hamsterzimmer()
    else:
      print("Du kannst auch gleich Winterschlaf machen, wie die Hamster von Ruiner.")
      print("\n")
      Hamsterzimmer()

  elif "2" in answer:
    print("Du schaust dich um, aber findest nichts interessantes.")
    print("\n")
    Hamsterzimmer()
  elif "3" in answer:
    Obergeschoss()
  else:
    print("Lösch dich, du Wiggsgrübbl.")
    print("\n")
    Hamsterzimmer()

def Altes_Streamzimmer():
  print("""Als du in den Raum gehst, fühlst du dich so, als würdest du ein Produktionszimmer für 
  Snuff-Filme betreten. Vor dir steht ein kleiner Holztisch, mit einer uralten weißen Tischdecke,
  daneben steht ein kaputter, von Staub und Flusen benetzter Bürostuhl ohne Rückenlehne. Die Wände sind
  deutlich sichtbar durchnässt (Schimmel ahoi), stellenweise mit schwarzen Graffitti bedeckt und hier
  und da hängen ein paar Boster von Kinderfilmen und Technobands. Nach rechts würde es in den letzten 
  Raum dieses "Hauses" gehen. Wenn hier die Rudi-Tapes nicht sind, dann können sie nur im Schlafzimmer 
  sein. Und wenn Rainer irgendwo ist, dann ist auch er da drin. Aber du findest in diesem alten Streamzimmer
  nichts interessantes. Hier hat zwar alles begonnen, du hast viele, lustige Erinnerungen an diesen Raum, 
  aber damit beschäftigst du dich jetzt nicht. Du machst dich bereit. Du sammelst noch einmal Mana. Willst
  du den Raum jetzt betretne?
  
  1. Rein da!
  2. Nein, lieber doch nicht.""")

  answer = input(RED).lower()
  print(Style.RESET_ALL)

  if "1" in answer:
    print("""Du bewegst dich lautlos durch den, mit einem Tuch verhangenen, Eingang ins Schlafzimmer. Es ist
    dunkel. Aber du hörst, ein leises Röcheln. Dann ein Knacken und ein Brummen. Neben dir ist ein Lichtschalter,
    willst du ihn betätigen? (J/N)""")

    answer = input(RED).lower()
    print(Style.RESET_ALL)

    if "j" in answer:
      print("""Du drückst den Lichtschalter. Das Licht geht an und entblößt vor dir das wahre Ausmaß, des eben
      gehörten. Vor dir siehst du ein Bett. Das Laken voller Flecken. Und darauf? Du kannst es kaum glaubne,
      auf dem Bett liegt er. Der Lügenlard. Der Suppengumbo. Der Speckbeppo. Das Arschgebirge wird nur durch eine,
      ebenfalls mit Flecken übsäte, Decke bedeckt. In seinem Arm hängt eine zusammengekauerte, nur noch spärlich mit
      Luft befüllte Gummipuppe. Wahrscheinlich seine Freundin aus Denken. Links von dir siehst du die fachmännisch (lel) 
      reparierte Balkontür. Ansonsten hast du das Gefühl, dass dieser Raum hier noch schlimmer und ekelerregender riecht, 
      als alle anderen Räume zusammne. Hier irgendwo müssen die Rudi-Tapes sein. Aber du musst ruhig sein. 
      Schlafende Hunde soll man nicht weckne. Was tust du?
      
      1. Unter das Bett schauen.
      2. Reiner weckne und ihm die Brügl naus schmeißen.
      3. Den einzigen Schrank im Zimmer begutachten.
      4. Wieder zurück in den Hausflur gehen.  """)

      answer = input(RED).lower()
      print(Style.RESET_ALL)

      if "1" in answer:
        print("""Du bückst dich und kriechst unter das Bett. Du schaust nicht so genau nach, was da alles auf dem
        Boden liegt, weil sonst müsstest du kotzne. Unter dem Bett findest du eine seltsame, metallische Box. Es ist
        ein Safe. Momentemol! Ein Safe? Was hat Reiner in einem Safe zu verstecken? Das muss es sein. Darin müssen
        die legendären Rudi-Tapes liegen. Du robbst dich weiter unter das Bett. Über dir bebt die Oberfläche. Ein 
        furchterregendes Grollen ertönt den Raum. Rainer fängt an zu schnarchen. Als du zum Safe vorgedrungen bist, verlangt er
        von dir eine vierstellige Zahl. Was tust du?
        
        1. Du gibst die Zahl ein.
        2. Dir entgleitet ein säuselndes "Keine, Ahnung , verdammte Aggst". """)

        answer = input(RED).lower()
        print(Style.RESET_ALL)

        if "1" in answer:
          print("\n")
          print("Gib die Zahl ein.")

          answer = input(RED).lower()
          print(Style.RESET_ALL)

          if "1510" in answer:
            print("\n")
            print("""Der Safe öffnet sich. Darin liegen tatsächlich eine Handvoll alter Videokasetten. 
            Eines trägt die Aufschrift "Familienausflug zu Mc Donald", ein weiteres verspricht einen "Lustigen Abend mit Rainer in der Badewanne".
            Du hast sie gefundne. Du hast die Rudi-Tapes wirklich gefundne. Du nimmst die Kasetten an dich und robbst wieder 
            unter dem Bett hervor. Als du dich langsam, mit den Kasetten in deiner Hose verstaut, aufrichtest, blickst du in die Augen
            des gerade wach werdenden Rainers, der langsam aber sicher realisiert, dass du nicht Hagen (der Wahnsinniche) bist. Was tust du?
            
            1. Du bekommst Panik und stolperst rücklings aus dem Zimmer, fängst dich aber und rennst los.
            2. Du willst mehr. Du hast zwar die Rudi-Tapes, aber du willst Rainer endlich eine Abreibung verpassne. Du kämpfst mit ihm.
            3. Du nimmst die Beine in die Hand, öffnest die Balkontür und verschwindest über den Balkon in die Freiheit.""")

            answer = input(RED).lower()
            print(Style.RESET_ALL)

            if "1" in answer:
              print("""Noch bevor du dich wieder aufraffst, ist der nackte Reiner vom Bett aufgesprungne und verfolgt dich. Du rennst los. Wohin rennst du?
              
              1. Die Treppe runter.
              2. Woanders hin. """)

              answer = input(RED).lower()
              print(Style.RESET_ALL)

              if "1" in answer:
                print("\n")
                game_over("""Du stürmst die Treppen runter. Rainer kommt brüllheulend hinter dir her. Du meddlst die Tür zum Hof raus
                und rennst zum Tor. Gerade als du über das Tor kletterst spürst du wie eine Aggst knapp deinen Kopf verfehlt.
                Doch du überlebst und rennst zu deinem Auto. Also du angekommen bist, fühlst du in deine Hose. Verdammt! Du hast die
                Tapes verloren! Alles umsonst! Oh nein. Du kannst jetzt nur noch berichtne, was auf den Tapes stand. Das macht dich aber 
                nur zu einem durchschnittlichen Haider. Du bist NICHT Derjeniche. Du hättest die Fassung behalten sollne.""")
              elif "2" in answer:
                game_over("""Du rennst wie ein kopfloses Huhn im Obergeschoss umher. Rainer holt dich schnaufend ein und nimmt dich in
                den Schwitzkasten. Der Geruch lässt dich ohnmächtig werdne. DEMJENICHEN wäre das nicht passiert.""")
              else:
                print("Du warst so nah dran. Verkagg es halt nicht.")
                print("\n")
                Obergeschoss()
            
            elif "2" in answer:
              print("""Du stellst dich dem Oger gegenüber. Er schnauft stark und schreit dich an. Sein Mundgeruch ist atemraubend.
              Jetzt bloß nichts falsches sagne. Du musst ihn beruhigen, um dann überraschend loszuschlagen. Du brauchst den 
              Überraschungsmoment, sonst kannst du den Oger nicht besiegne. Was sagst du um Reiner zu besänftigen?
              
              1. "Spielt einer von euch eigentlich Killing Floor?"
              2. "Herr Winklaaaa, können wir normal mitnander redne?"
              3. "Eh Mallah." """)

              answer = input(RED).lower()
              print(Style.RESET_ALL)

              if "1" in answer:
                print("\n")
                game_over("""Du wusstest es. Du hast es immer gewusst. Rainer rastet sofort aus mit einem "Wie bidde?!" und schmeißt dir die 
                Brügl naus. RIP.""")
              elif "2" in answer:
                print("\n")
                game_over("Du hast keine Chongze, Rainer prügelt dir so die Scheiße raus, dass du nie wieder aufstest. RIP.")
              elif "3" in answer:
                print("\n")
                game_over("Guter Versuch, aber mit Rainer lässt sich nicht redne. Er schmeißt dir die Brügl naus. RIP.")
              else: 
                print("\n")
                secret_ending()
            
            elif "3" in answer:
              print("\n")
              game_over("""Du reißt die Balkontür auf, die frische Luft von draußen ist fast schon erlösend. Du schwingst dich über das Geländer
              und springst gekonnt nach unten. Dann noch über den Zaun. Geschafft. Rainer steht oben am Balkon und schreit dir hinterher.
              Als du zu deinem Auto kommst, bemerkst du, dass du die Hälfte der Rudi-Tapes bei dem Sprung vom Balkon verloren hast.
              Das ist sehr ärgerlich! Damit kannst du sicherlich das Game für einige Monate befeuern, aber beenden kannst du es nicht. 
              Zurückgehen kannst du auch nicht. Du zweifelst. Bist du wirklich Derjeniche? Hätte Derjeniche nur die Hälfte der Tapes geborgne?
              Was hättest du anders machen können? Du fährst los und überlegst. Vielleicht kommst du eines Tages wieder.""")
            
            else:
              print("Noob! Geh sterbne, wenn du nichtmal diese Aufgabe lösne kannst!")
              print("\n")
              Obergeschoss()
          else:
            game_over("Wenn du nicht mal das kannst, hast du hier nix verlorne!")
          
        elif "2" in answer:
          print("\n")
          game_over("""Als dir die Worte entgleiten, spürst du wie die Ebene über die erzittert. Du hast den Drachen geweckt. Oder?
          Irgndetwas hast du ausgelöst. Die Beule über dir wird immer größer und größer. Oh  nein, Rainer dreht sich im Bett! Auf einmal
          fängt das Bettgestell an zu knarzen. Du vernimmst ein brechen von Holz. Du schaust über dich, als es schon zu spät ist. Die Latten
          des Rosts gebne nach und die Matratze, samt 267kg Mettmasse stürzne auf dich herab. Als du dein Lebne aushauchst hörst du noch ein 
          leises "Aleggsa, schalt das Studio auf weiß...Aleggsaaaa!" """)
        else:
          print("\n")
          game_over("Der Wingl wonglt, aber was machst du???")

      elif "2" in answer:
        print("\n")
        game_over("Das ist nicht deine Aufgabe als DERJENICHE! Du bist wegen etwas anderm hier, verdammte Aggst!")

      elif "3" in answer:
        print("""Du durchwühlst den Schrank. Aber du findest nichts wertvolles. Aber doch, was ist das? Ein Zettel?
        Auf dem Zettel steht "alfanumerisches Paswort" und "Drachenlord123". Wofür kann das wohl gut sein? Du gehst wieder zurück
        zum alten Streamzimmer (schlampiges Spieldesign, tz). """)
        print("\n")
        Altes_Streamzimmer()
      elif "4" in answer:
        Obergeschoss()
      else:
        print("Junge, ohne Wodde... ")
        print("\n")
        Obergeschoss()

    elif "n" in answer:
      print("""Es bleibt dunkel im Zimmer. Du kannst nur erahnen, was vor dir liegt. Das hat so keinen Sinn, du gehst zurück in den
      Flur.""")
      Obergeschoss()  
    else:
      print("\n")
      game_over("Ich bin ned der Drache, verdammte Aggst! Trotzdem hau ich dir den Bannhammer raus!")
  
  elif "2" in answer:
    print("Pussy!")
    print("\n")
    Obergeschoss()
  else:
    print("Weißt du was, du Huansohn...")
    print("\n")
    Obergeschoss()

def secret_ending():
  print("\n")
  print("""Du überlegst nochmal kurz und dir ist bewusst, dass nichts davon Rainer beruhigen kann. Stattdessen nimmst du die Fäust in die Hand
  und gehst direkt auf Rainer los. Den ersten Schlag wehrt er mit einem gekonnten Roundhouse Kigg ab. Den zweiten Schlag steckt er ein. BÄM!
  Volles Pfund in die Fresse. Er weicht kurz zurück, sammelt Mana und fängt daraufhin an gold zu leuchtne. Ihr prügelt euch wie echte Männer.
  BANG! POW! BUMM! Jeder von euch kassiert Schläge des anderen.
  
  Haha, natürlich nur Spaß. Als Rainer deinen ersten Schlag ins Gesicht bekommt, der zudem nur schwach und gestreift war, bricht er heulend
  zusammen und hält sich die Wange. "Die Haider wollne mich tötne." kreischt er dich an. Da liegt er nun, der mächtige Drachenlord. In seinem eigenen
  Kot. Zusammengekauert, besiegt. Von wegne sechs Jahre Kampfsport. Er hat rein gar nichts drauf. Du nimmst die Rudi-Tapes und läufst genüglich aus
  der Schanze heraus. Bummsdi ist mit seiner Situation eh schon gestraft genug. Du lässt ihn in Frieden zurück. Du hast was du willst. Als du in dein Auto
  steigst, hörst du ihn von seinem Balkon aus hinter dir herrufen: "Na, komm doch her, du Feigling! Ihr werdet mich niemals besiegne. Komm doch
  her und trau dich! Du feiger Hurensohn!!!!" Es ist alles wie immer. Du lächelst, weil du die Macht in der Hand hälst, das Game zu beendne. Du bist
  wahrhaftig:
  
  DERJENICHE *holy music intesifies*
  
  SIEG""")

def Easteregg():
  print("""Du öffnest den Safe. Darin befinden sich zwar keine Rudi Tapes, dafür aber etwas anderes. Du nimmst ein kleines Buch heraus.
  Du blätterst darin. Es ist ein altes Tagebuch von Reiner. Viel belangloses Zeug über die Haider. Aber eine Stelle macht dich neugierig. 
  Am 15.10.2016 steht in einem Eintrag: "Hallo lipes Tagebuch. Ich habe heute den Haidern gesacht das ich bi bin aber das stimt gar nicht
  ich habe sie damit belogne. Ich mag nur frauen hate aber noch nie eine. Das macht mich ganz truarig." Du kannst dir das Lachen nicht verkneifen.
  Das sind zwar nicht die Rudi-Tapes, aber das generiert Mett für Jahre. Endlich ist diese Frage geklärt: Rainer ist NICHT bi! Du kannst nicht
  aufhören zu lachen und schaust dich weiter im Zimmer um.""")
  print("\n")

  Wohnarbeitsspielküche()

# Das Spiel starten
Vor_der_Schanze()