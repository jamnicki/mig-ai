# MigAI - the Sign Language Translation
> https://migai-pnw-site.streamlit.app/

<div align="center">
   <img src="https://github.com/jamnicki/MigAI/assets/56606076/9cd1dbc7-b402-47a4-b4b9-f8538bd8c5a3" width="70%">
<!--   ![MigAI_logo_big](https://github.com/jamnicki/MigAI/assets/56606076/9cd1dbc7-b402-47a4-b4b9-f8538bd8c5a3) -->
</div>

## Introduction
Deaf people face significant challenges in everyday communication, especially with those who do not know sign language. The lack of an interpreter during key interactions exacerbates this gap, highlighting the need for innovative solutions. A Polish sign language translation system can revolutionize deaf people's interactions, offering them better access to information and eliminating communication barriers, significantly simplifying daily life.

![app_view](https://github.com/user-attachments/assets/be3a49be-441d-4899-813b-ef38e0018c38)

## Data
The data used for the project comes from two sources. The first is the Repository of the Polish Sign Language Corpus [2]. This is a collection of over 700 recordings of sign utterances that have translations in Polish. In addition, the collection was expanded with data from the Corpus Dictionary of Polish Sign Language [1], which provided more than 2,000 recordings showing the use of definitions in context.

## Method Description
To solve the problem first, key points corresponding to the positions of body parts were extracted from the recordings using the MediaPipe model. Based on these points, two translation models were developed: Seq2Seq and Transformer [3,4].
![metoda](https://github.com/user-attachments/assets/2bf57d30-cc10-481c-82d1-e1a759839939)

## Evaluation
Based on the tests conducted, the translation quality of two models was compared: Seq2Seq and Transformer, using three metrics: BLEU, METEOR, and TER. In addition, the result of the project was presented to members of the Lower Silesia Branch of the Polish Association of the Deaf, where feedback and suggestions on the developed system were obtained.

## Results
For each of the tested architectures, the parameter configuration that achieved the best results on the validation set was selected. The Transformer model significantly outperformed the Seq2Seq solution due to its ability to analyze and learn complex relationships specific to sign language and its contextual nature. The graph below shows the performance of both models on the test set.

![hist](https://github.com/user-attachments/assets/c23551f2-fc94-4459-bd7d-958efa89b000)

> BLEU measures the coverage of translation n-grams with a reference value. METEOR, a modified BLEU metric that takes into account synonyms and sentence structure. TER determines the number of edits needed to achieve a correct translation.

![wyniki_tab](https://github.com/user-attachments/assets/ad48aa8c-5f53-4544-aaa8-f1830da79410)

---

The project paves the way for further research into the development of more advanced and accurate translation tools that can make a significant difference in the lives of the deaf community.


## 🥇 Contributors
<a href="https://github.com/jamnicki/mig-ai/graphs/contributors">
   <img src="https://contrib.rocks/image?repo=jamnicki/mig-ai"/>
</a>


## Patrons
![partners](https://github.com/user-attachments/assets/a0d181b0-acab-4c30-95f9-26874c5e43e8)


<!--
<div align="center">
  <img src="https://github.com/jamnicki/mig-ai/assets/56606076/1bf2f7f8-07d7-45e4-a853-00fcf2947a91" height="60">
  <img src="https://github.com/jamnicki/mig-ai/assets/56606076/514f1729-3db1-409b-a9e3-75dab11ee85f" height="60">
</div>
-->


## References

[1] Łacheta, J., Czajkowska-Kisil, M., Linde-Usiekniewicz, J., Rutkowski, P., Korpusowy słownik polskiego języka migowego (Wydział Polonistyki Uniwersytetu Warszawskiego, Warszawa, 2016). Publikacja online

[2] Rutkowski, P., Łozińska, S., Filipczak, J., Łacheta, J., Mostowski, P., Jak powstaje korpus polskiego języka migowego (pjm)

[3] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L., Polosukhin, I., Attention is all you need.

[4] Sutskever, I., Vinyals, O., Le, Q.V., Sequence to sequence learning with neural networks, CoRR. 2014, tom abs/1409.3215.

[5] Lugaresi, C., Tang, J., Nash, H., McClanahan, C., Uboweja, E., Hays, M., Zhang, F., Chang, C., Yong, M.G., Lee, J., Chang, W., Hua, W., Georg, M., Grundmann, M., Mediapipe: A framework for building perception pipelines, CoRR. 2019

---

> Research carried out as part of the "Research and Implementation Project" course for the Artificial Intelligence major in the 23/24 academic year. Project carried out in cooperation with the Sign Linguistics Laboratory at the University of Warsaw.

