# Aqueous solubility prediction

Fast aqueous solubility prediction based on the Molecule Attention Transformer (MAT). The authors used AqSolDB to fine-tune the MAT network to solubility prediction, achieving competitive scores in the Second Challenge to Predict Aqueous Solubility (SC2).

## Identifiers

* EOS model ID: `eos6oli`
* Slug: `soltrannet-aqueous-solubility`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Experimental value`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Predicted LogS (log of the solubility)

## References

* [Publication](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00331)
* [Source Code](https://github.com/gnina/SolTranNet)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos6oli)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6oli.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos6oli) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00331) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a Apache-2.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!