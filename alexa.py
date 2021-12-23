if __name__ == "__main__":
    import json
    style_check_text = json.load(open("alexa.json"))
    percent_ratings = []
    feedback_ready = False
    feedback = []
    for item in style_check_text['TextDetections']:
      if item['DetectedText'][-1] == '%':
        percent_ratings.append(item['DetectedText'])
      if feedback_ready == True and not item['DetectedText'] == 'STYLE' and not item['DetectedText'] == 'CHECK' and not item['DetectedText'] == 'COLOR':
        feedback.append(item['DetectedText'])
      if item['DetectedText'] == 'look:':
        feedback_ready = True
    feedback = ' '.join(feedback)
    rating1 = int(percent_ratings[-2][:-1])
    rating2 = int(percent_ratings[-1][:-1])
    if rating1 > rating2:
      alexa_verbal_output = 'The first outfit looks better. ' + str(rating1) + ' percent to ' + str(rating2) + ' percent. '
    else:
      alexa_verbal_output = 'The second outfit looks better. ' + str(rating2) + ' percent to ' + str(rating1) + ' percent. '
   alexa_verbal_output = alexa_verbal_output + feedback
  print(alexa_verbal_output)
  f = open('alexa.txt', 'w')
  f.write(alexa_verbal_output)
  f.close()
