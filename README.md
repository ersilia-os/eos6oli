# Aqueous solubility prediction

## Model Identifiers
- Slug: soltrannet-aqueous-solubility
- Ersilia ID: eos6oli
- Tags: LogS,	physchem,	ADMET

## Model Description
A machine learning tool for fast aqueous solubility prediction
- Input: SMILES
- Output: Probability (Probability of Log S > -4)
- Model type: Classification
- Mode of Training: Pretrained
- Training data: 9,982 compounds (https://github.com/francoep/SolTranNet_paper/blob/main/soltrannet_data.tar.gz)
- Experimentally validated: No

## Source code
This model was published by Paul G. Francoeur and David R. Koes. SolTranNet–A Machine Learning Tool for Fast Aqueous Solubility Prediction. *J. Chem. Inf. Model.* 2021, 61, 6, 2530–2536. DOI:https://doi.org/10.1021/acs.jcim.1c00331
- Code: https://github.com/gnina/SolTranNet
- Chedkpoints: https://github.com/gnina/SolTranNet/blob/main/soltrannet/soltrannet_aqsol_trained.weights

## License
The Apache 2.0 license applies to all parts of the repository. This repository uses the externally maintained library "SolTraNet", located at `/model` and licensed under a Apache 2.0 License

## History
This model was downloaded and incorporated ion October 19, 2021
