# SAR despeckling via regional denoising diffusion probabilistic model

A conditional denoising diffusion probabilistic model (DDPM) for SAR despeckling.

## Requirements

```bash
pip install -r requirements.txt
pip install huggingface_hub   # for downloading pretrained weights
```

## Dataset Preparation

Organize your dataset in the following structure:

```
data/
├── train/
│   ├── input/      # degraded images
│   └── target/     # clean ground-truth images
└── test/
    ├── input/      # degraded images
    └── target/     # clean ground-truth images (required by the dataloader)
```

- Filenames in `input/` and `target/` must be **paired in sorted order**.
- For inference, image dimensions should be multiples of 16 (the dataloader will auto-resize if not).
- For preprocessing utilities (noise addition, format conversion), see `scripts/`.

## Training

```bash
python train_diffusion.py --config configs.yml
```

- Checkpoints are saved to `checkpoints/` every `snapshot_freq` steps.
- Validation patches are saved to `validation/` every `validation_freq` steps.
- Training resumes automatically if a checkpoint exists at `training.resume`.

## Pretrained Weights

Pretrained weights are hosted on Hugging Face: [Teriri1999/R-DDPM](https://huggingface.co/Teriri1999/R-DDPM)

Download with Python:

```python
from huggingface_hub import hf_hub_download

hf_hub_download(
    repo_id="Teriri1999/R-DDPM",
    filename="diffusion_model.pth",
    local_dir="checkpoints/",
)
```

Or via the CLI:

```bash
huggingface-cli download Teriri1999/R-DDPM diffusion_model.pth --local-dir checkpoints/
```

## Inference

```bash
python eval_diffusion.py --config configs.yml
```

Restored images are saved to `results/`. Each image is processed using overlapping patches (stride = `grid_r`) and averaged at overlapping regions.

## Evaluation

After inference, compute PSNR and SSIM against ground-truth:

```bash
python calculate_psnr_ssim.py
```

## Citation

If you find this work useful, please cite:

```bibtex
@inproceedings{hu2024sar,
  title={SAR despeckling via regional denoising diffusion probabilistic model},
  author={Hu, Xuran and Xu, Ziqiang and Chen, Zhihan and Feng, Zhenpeng and Zhu, Mingzhe and Stankovi{\'c}, Ljubi{\v{s}}a},
  booktitle={IGARSS 2024-2024 IEEE International Geoscience and Remote Sensing Symposium},
  pages={7226--7230},
  year={2024},
  organization={IEEE}
}
```

