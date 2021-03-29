# Your Speech Recognition

Easy way to fine tune [DeepSpeech](https://github.com/mozilla/DeepSpeech)
voice recognition to your voice by making a website to do it
all for you. Why? Because I couldn't swear, it got distracted by my
static voice due to mic issues (unlike Siri),
and I wanted an automated way for me to train the data rather than constantly
finding something to say then writing it down.

By: [Andrew-Chen-Wang](https://github.com/Andrew-Chen-Wang)

Date Created: 28 March 2020

---
### Requirements

- Python 3.x (Mac has this installed already)

For the voice recognition:
- Portaudio

---
### Usage

1. Run in your terminal or command prompt, depending on your system:
    - Windows: `virtualenv venv && venv\Scripts\activate`
    - Mac/Linux: `virtualenv venv && source venv/bin/activate`
2. First you need to prepare some data for training. Run: 
   `python app.py`
3. Open your browser, head to the website http://localhost:5000/ and follow
   the instructions on the website.
4. Now it's time for the "machine learning." Depending on your system:
    - Mac/Linux: `sh train.sh`
    - Note: You can specify some other parameters via the scripts or by
      yourself via your terminal/command-prompt.
5. Finally, you can run the voice recognition software. Depending on your system: 

Windows:
```shell
python recognizer.py -w media \
--model output_models\deepspeech-0.9.3-models.pbmm \
--scorer models\deepspeech-0.9.3-models.scorer
```

Mac/Linux:
```shell
python recognizer.py -w media \
--model output_models/deepspeech-0.9.3-models.pbmm \
--scorer models/deepspeech-0.9.3-models.scorer
```

Now, just talk and see the output working!

---
### TODO

- Need to write the website for collecting user speech
- Allow the website to also do "VAD" by making audio files by
  intervals of 1.75 seconds during recording. Unfortunately,
  I don't think we can do automatic detection and
  thus humans will think of the software poorly, but at 
  least it somewhat works.
- Actually write the NT script for training.
- Compare the amount of time required for this to be pretty good. I.e. 
  check if 30 minutes of training, an hour, etc. is the marginal benefit 
  worth the trouble of more effort?

---
### License

```text
Copyright 2021 Andrew Chen Wang

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
