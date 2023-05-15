# Make it more memory efficient by monkey patching the LLaMA model with XFormer's
# memory-efficient attention.
# Use this one instead train_mem.py if you are training on V100.

# Need to call this before importing transformers.
from fastchat.train.llama_xformer_monkey_patch import (
    replace_llama_attn_with_xformer
)
from fastchat.train.hf_save_model_monkey_patch import (
    replace_hf_save_model
)


if __name__ == "__main__":
    replace_llama_attn_with_xformer()
    replace_hf_save_model()
    from fastchat.train.train import train
    train()
