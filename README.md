# Aqueous solubility prediction

Fast aqueous solubility prediction based on the Molecule Attention Transformer (MAT). The authors used AqSolDB to fine-tune the MAT network to solubility prediction, achieving competitive scores in the Second Challenge to Predict Aqueous Solubility (SC2).

This model was incorporated on 2021-10-19.

## Information
### Identifiers
- **Ersilia Identifier:** `eos6oli`
- **Slug:** `soltrannet-aqueous-solubility`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Not Applicable`
- **Tags:** `Solubility`, `ADME`, `LogS`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Predicted LogS (log of the solubility)

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| solubility | float | low | Predicted solubility in LogS |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos6oli](https://hub.docker.com/r/ersiliaos/eos6oli)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6oli.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6oli.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `5669`
- **Image Size (Mb):** `5576.54`

**Computational Performance (seconds):**
- 10 inputs: `34.08`
- 100 inputs: `24.47`
- 10000 inputs: `476.4`

### References
- **Source Code**: [https://github.com/gnina/SolTranNet](https://github.com/gnina/SolTranNet)
- **Publication**: [https://pubs.acs.org/doi/10.1021/acs.jcim.1c00331](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00331)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos6oli
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos6oli
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
