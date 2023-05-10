# DanAndersson2023-1 Droplet Microfluidics

Droplet Microfluidics for detection of bacterial heteroresistance

## Installation

Install the [conda](https://conda.io) package, dependency and environment manager.

Then create the `droplet_microfluidics` conda environment:

    cd <path to your 'DanAndersson2023-1' directory>
    conda env create -f environment.yml

This will install all necessary project dependencies.

## Usage

Copy all project data to the [data](data) directory (or use symbolic links).

Then run [Jupyter Lab](https://jupyter.org) from within the `droplet_microfluidics` conda environment:

    cd <path to your 'DanAndersson2023-1' directory>
    conda activate droplet_microfluidics
    jupyter-lab

All analysis notebooks can be found in the [notebooks](notebooks) directory.

## Support

If you find a bug, please [raise an issue](https://github.com/BIIFSweden/DanAndersson2023-1/issues/new).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

[SciLifeLab BioImage Informatics Facility (BIIF)](https://biifsweden.github.io) project lead: Jonas Windhager

## License

[MIT](LICENSE)
