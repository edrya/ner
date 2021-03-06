from __future__ import print_function
import semantria
import uuid
import time
import requests

serializer = semantria.JsonSerializer()

session = semantria.Session("59e4e96b-f19b-48b5-910a-a2b5d9d2bfc7", "0cee133a-889e-4d1f-9d99-2749677bcfdd",
                            serializer,
                            use_compression=True)

initialTexts = [
    """BASEBALL - DODGERS WIN FIFTH STRAIGHT .
MONTREAL 1996-08-28
Hideo Nomo allowed a run in seven innings for his fifth win in seven road starts and Greg Gagne capped a three-run fourth with a two-run homer as the Los Angeles Dodgers claimed a 5-1 victory the Montreal Expos on Tuesday .
With their fifth straight win , the Dodgers moved a half-game ahead of the Expos at the top of the wild card hunt behind Nomo ( 13-10 ) , who allowed six hits and walked four with six strikeouts .
In San Francisco , Mike Williams allowed two runs in 7-1/3 innings and Benito Santiago and Ruben Amaro had RBI hits in the first inning as the Philadelphia Phillies edged the San Francisco Giants 3-2 .
Williams ( 5-12 ) , who snapped a personal three-game losing streak , allowed five hits , walked two and struck out five .
It was also Williams ' first win in three career decisions against San Francisco .
In Pittsburgh , Al Martin's run-scoring single snapped a fifth-inning tie and Denny Neagle outdueled John Smoltz as the Pittsburgh Pirates edged the Atlanta Braves 3-2 .
The Braves led 2-1 entering the fifth , but the Pirates pushed across two runs against Smoltz ( 20-7 ) .
Neagle ( 14-6 ) beat the Braves for the third time this season , allowing two runs and six hits in eight innings .
In St Louis , Gary Sheffield and Devon White each drove in two runs and Mark Hutton scattered four hits over six innings to lead the Florida Marlins past the St. Louis Cardinals 6-3 .
White added a solo homer , his 11th , off reliever Mark Petkovsek with one out in the fifth , giving the Marlins a 6-0 lead .
In New York , Steve Finley's three-run homer capped a four-run eighth inning and gave the San Diego Padres a 4-3 victory over New York , spoiling Bobby Valentine's debut as Mets ' manager .
The rally made a winner out of reliever Willie Blair
Tony Gwynn and Wally Joyner had two hits apiece , helping the Padres to their third straight win .
First-place San Diego has won seven of its last eight games and improved to 34-20 against NL East opponents .
In Houston , Tony Eusebio's eighth-inning sacrifice fly capped a comeback from a five-run deficit that gave the Houston Astros a 6-5 victory over the Chicago Cubs .
The Astros trailed 5-0 after three innings , but scored three runs in the fourth and one in the sixth before taking the lead in the eighth .
In St Louis , Gary Sheffield and Devon White each drove in two runs and Mark Hutton scattered four hits over six innings to lead the Florida Marlins past the St. Louis Cardinals , 6-3 ,
Sheffield , who was benched Monday , delivered a double down the left-field line in the first , scoring Luis Castilla and Alex Arias to put the Marlins ahead to stay .
At Colorado , Hal Morris and Eric Davis each homered and John Smiley scattered six hits over 6 2/3 innings as the Cincinnati Reds defeated the Colorado Rockies 4-3 , snapping a four-game losing streak .
The Reds took a one-run lead in the second inning when Morris led off with his 10th homer off starter Armando Reynoso ( 8-9 ) .
They increased their bulge to 4-0 in the third when Barry Larkin drew a one-out walk , Kevin Mitchell singled and Davis launched his 22nd homer over the right-field wall .""",
    "On this day in 1786 - In New York City  commercial ice cream was manufactured for the first time."

]



for text in initialTexts:
    doc = {"id": str(uuid.uuid4()).replace("-", ""), "text": text}
    status = session.queueDocument(doc)
    if status == 202:
        print("\"", doc["id"], "\" document queued successfully.", "\r\n")

length = len(initialTexts)
results = []

while len(results) < length:
    print("Retrieving your processed results...", "\r\n")
    time.sleep(2)
    # get processed documents
    status = session.getProcessedDocuments()
    results.extend(status)

for data in results:
    # print document sentiment score
    print("Document ", data["id"], " Sentiment score: ", data["sentiment_score"], "\r\n")

    # print document themes
    if "themes" in data:
        print("Document themes:", "\r\n")
        for theme in data["themes"]:
            print("     ", theme["title"], " (sentiment: ", theme["sentiment_score"], ")", "\r\n")

    # print document entities
    if "entities" in data:
        print("Entities:", "\r\n")
        print (len(data["entities"]))
        for entity in data["entities"]:
            print("\t", entity["title"], " : ", entity["entity_type"], " (sentiment: ", entity["sentiment_score"], ")",
                  "\r\n")
