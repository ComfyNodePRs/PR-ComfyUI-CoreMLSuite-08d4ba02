import torch

from comfy import supported_models_base
from comfy import latent_formats
from comfy.model_detection import convert_config

SD15 = {
    "use_checkpoint": False,
    "image_size": 32,
    "out_channels": 4,
    "use_spatial_transformer": True,
    "legacy": False,
    "adm_in_channels": None,
    "dtype": torch.float16,
    "in_channels": 4,
    "model_channels": 320,
    "num_res_blocks": 2,
    "attention_resolutions": [1, 2, 4],
    "transformer_depth": [1, 1, 1, 0],
    "channel_mult": [1, 2, 4, 4],
    "transformer_depth_middle": 1,
    "use_linear_in_transformer": False,
    "context_dim": 768,
    "num_heads": 8,
    "disable_unet_model_creation": True,
}


def get_unet_config():
    return convert_config(SD15)


def get_model_config():
    config = supported_models_base.BASE(get_unet_config())
    config.latent_format = latent_formats.SD15()
    return config