# Attention-Based-Dynamic-Graph-Learning-Framework-for-Asset-Pricing
This is a tensorflow-keras implementation of our CIKM-2021 paper [**"Attention Based Dynamic Graph Learning Framework for Asset Pricing"**](https://dl.acm.org/doi/abs/10.1145/3459637.3482413)

 ![GitHub Dark](Figures/Attention_diffusion.png)


### **Requirments** 
- numpy >= 1.19
- pandas >= 1.0.1
- sckitlearn >= 0.22.0
- matplotlib >= 3.1.0
- pyreadr >= 0.4.0
- tensorflow == 2.5.0
- keres == 2.3.1




### **DATA** 

The initial raw daily data can be downloaded from [Here](https://drive.google.com/file/d/15HG7-P5hUU8TtRmMDzY3_j_k-h_jyGwJ/view?usp=sharing). Caution this data set is very large about 330mb and consist of 3147312 rows and 14 colums. The data includes 1035 unique TIC id for firms.
Running the [Data_clean.py][Data_clean.py] will produce a clean pickle file namely daily_clear_ret.pickle with pandas data frame. 
The clean data shape is (928773, 27), with 25 features and TIC and CUSIP as identifying variable. 


### The Model
A Keras implementation of the Dy-Gap model proposed in the paper is presented in [Dy_Gap_Model.ipynb](Dy_Gap_Model.ipynb). 



### Citation
@inproceedings{10.1145/3459637.3482413,
author = {Uddin, Ajim and Tao, Xinyuan and Yu, Dantong},
title = {Attention Based Dynamic Graph Learning Framework for Asset Pricing},
year = {2021},
isbn = {9781450384469},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3459637.3482413},
doi = {10.1145/3459637.3482413},
abstract = {Recent studies suggest that financial networks play an essential role in asset valuation and investment decisions. Unlike road networks, financial networks are neither given nor static, posing significant challenges in learning meaningful networks and promoting their applications in price prediction. In this paper, we first apply the attention mechanism to connect the "dots" (firms) and learn dynamic network structures among stocks over time. Next, the end-to-end graph neural networks pipeline diffuses and propagates the firms' accounting fundamentals into the learned networks and ultimately predicts stock future returns. The proposed model reduces the prediction errors by 6% compared to the state-of-the-art models. Our results are robust with different assessment measures. We also show that portfolios based on our model outperform the S&P-500 index by 34% in terms of Sharpe Ratio, suggesting that our model is better at capturing the dynamic inter-connection among firms and identifying stocks with fast recovery from major events. Further investigation on the learned networks reveals that the network structure aligns closely with the market conditions. Finally, with an ablation study, we investigate different alternative versions of our model and the contribution of each component.},
booktitle = {Proceedings of the 30th ACM International Conference on Information & Knowledge Management},
pages = {1844–1853},
numpages = {10},
keywords = {asset pricing, fintech, graph neural networks, diffusion recurrent convolution, graph attention, stock price prediction},
location = {Virtual Event, Queensland, Australia},
series = {CIKM '21}
}

  

