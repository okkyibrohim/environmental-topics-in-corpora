# Environmental Topics in Corpora

## About this corpora
Here we provide several datasets for Twitter analysis about environmental topics. There are three datasets with the short information as follows:
* [Italian Stance Detection](https://github.com/okkyibrohim/environmental-topics-in-corpora/tree/main/masked_dataset/masked_italian_stance_detection): An Italian Twitter dataset for stance detection in the natural environment topics.
* [Italian Structured Sentiment Analysis](https://github.com/okkyibrohim/environmental-topics-in-corpora/tree/main/masked_dataset/masked_italian_structured_sa): An Italian Twitter dataset for structured sentiment analysis in the natural environment topics.
* [English Sentiment Term Extraction](https://github.com/okkyibrohim/environmental-topics-in-corpora/tree/main/masked_dataset/masked_english_sentiment_term_extraction): An English Twitter dataset for sentiment term extraction in the natural environment topics.

For more explanation about structured sentiment analysis and sentiment term extraction, you can read our [annotation guidelines](https://github.com/okkyibrohim/environmental-topics-in-corpora/tree/main/annotator_guidelines).

Due to [Twitter's Terms of Service (now X)](https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases), we cannot provide the hydrated tweets directly to the public, so in this case, we masked all usernames and URLs with asterisks (`*`). However, the policy still allows us to share the hydrated tweets for non-commercial research purposes. If you need the original tweets for non-commercial research purposes but you cannot re-scrape them, feel free to request by email to us at [muhammadokky.ibrohim@unito.it](mailto:muhammadokky.ibrohim@unito.it).

## About agreement evaluation code
If annotate a new dataset following our annotation scheme and the same [annotation tool](https://annotate.langing.ai/), you can use our script to evaluate the agreement level of your annotation result. The script is implemented on `Python 3` and requires a number of packages. To install all needed packages, simply run `$ pip install -r requirements.txt` in your virtual environment. To use the script, simply call the evaluation metric function and put the parameters needed.

## More detail
If you want to know more about the dataset including how we built it and the agreement evaluation results, please read them in our paper (the paper link will be given soon once the paper is published in [CLiC-it 2023](https://clic2023.ilc.cnr.it/).

## Citation
The code and the data in this repository can be used for free, but if you want to publish a paper/publication using this code/data, please cite this publication: **Cristina Bosco, Muhammad Okky Ibrohim, Valerio Basile, Indra Budi. 2023. How green is Sentiment Analysis? Environmental Topics in Corpora at the University of Turin. In: *Proceeding of CLiC-it 2023*. [to be published]** (Every paper template may have different citation writing. The .bib citation will be provided soon after the paper is published).

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
