import json
import os

cells = [
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import cv2\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "def show_results(img_color_orig, img_gray_orig, img_gray_enh, img_color_enh, title):\n",
            "    fig, axs = plt.subplots(2, 2, figsize=(10, 8))\n",
            "    fig.suptitle(title, fontsize=16)\n",
            "    \n",
            "    axs[0, 0].imshow(cv2.cvtColor(img_color_orig, cv2.COLOR_BGR2RGB))\n",
            "    axs[0, 0].set_title('Original Colorida')\n",
            "    axs[0, 0].axis('off')\n",
            "    \n",
            "    axs[0, 1].imshow(img_gray_orig, cmap='gray')\n",
            "    axs[0, 1].set_title('Original em Escala de Cinza')\n",
            "    axs[0, 1].axis('off')\n",
            "    \n",
            "    axs[1, 0].imshow(img_gray_enh, cmap='gray')\n",
            "    axs[1, 0].set_title('Realçada em Escala de Cinza')\n",
            "    axs[1, 0].axis('off')\n",
            "    \n",
            "    axs[1, 1].imshow(cv2.cvtColor(img_color_enh, cv2.COLOR_BGR2RGB))\n",
            "    axs[1, 1].set_title('Realçada Colorida')\n",
            "    axs[1, 1].axis('off')\n",
            "    \n",
            "    plt.tight_layout()\n",
            "    plt.show()\n",
            "\n",
            "img_color = cv2.imread('gato.jpg')\n",
            "img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# a) Negativo da imagem\n",
            "def negative_transform(img):\n",
            "    return 255 - img\n",
            "\n",
            "gray_neg = negative_transform(img_gray)\n",
            "color_neg = negative_transform(img_color)\n",
            "show_results(img_color, img_gray, gray_neg, color_neg, \"a) Negativo\")\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# b) Alongamento de contraste (contrast stretching)\n",
            "def contrast_stretching(img, c=0, d=255):\n",
            "    a = np.min(img)\n",
            "    b = np.max(img)\n",
            "    img_stretched = (img.astype(float) - a) * ((d - c) / (b - a + 1e-6)) + c\n",
            "    return np.clip(img_stretched, 0, 255).astype(np.uint8)\n",
            "\n",
            "gray_cs = contrast_stretching(img_gray, 0, 255)\n",
            "color_cs = contrast_stretching(img_color, 0, 255)\n",
            "show_results(img_color, img_gray, gray_cs, color_cs, \"b) Alongamento de Contraste\")\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# c) Realce linear\n",
            "def linear_transform(img, alpha, beta):\n",
            "    res = alpha * img.astype(float) + beta\n",
            "    return np.clip(res, 0, 255).astype(np.uint8)\n",
            "\n",
            "gray_lin = linear_transform(img_gray, 1.5, 40)\n",
            "color_lin = linear_transform(img_color, 1.5, 40)\n",
            "show_results(img_color, img_gray, gray_lin, color_lin, \"c) Realce Linear\")\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# d) Realce logarítmico\n",
            "def log_transform(img, c):\n",
            "    res = c * np.log(1 + img.astype(float))\n",
            "    return np.clip(res, 0, 255).astype(np.uint8)\n",
            "\n",
            "c_gray = 255.0 / np.log(1 + np.max(img_gray.astype(float)))\n",
            "c_color = 255.0 / np.log(1 + np.max(img_color.astype(float)))\n",
            "gray_log = log_transform(img_gray, c_gray)\n",
            "color_log = log_transform(img_color, c_color)\n",
            "show_results(img_color, img_gray, gray_log, color_log, \"d) Realce Logarítmico\")\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# e) Realce quadrático\n",
            "def quadratic_transform(img, c):\n",
            "    res = c * (img.astype(float) ** 2)\n",
            "    return np.clip(res, 0, 255).astype(np.uint8)\n",
            "\n",
            "gray_quad = quadratic_transform(img_gray, 1.0 / 255.0)\n",
            "color_quad = quadratic_transform(img_color, 1.0 / 255.0)\n",
            "show_results(img_color, img_gray, gray_quad, color_quad, \"e) Realce Quadrático\")\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# f) Realce por raiz quadrada\n",
            "def sqrt_transform(img, c):\n",
            "    res = c * np.sqrt(img.astype(float))\n",
            "    return np.clip(res, 0, 255).astype(np.uint8)\n",
            "\n",
            "gray_sqrt = sqrt_transform(img_gray, 255.0 / np.sqrt(255.0))\n",
            "color_sqrt = sqrt_transform(img_color, 255.0 / np.sqrt(255.0))\n",
            "show_results(img_color, img_gray, gray_sqrt, color_sqrt, \"f) Raiz Quadrada\")\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# g) Correção gama\n",
            "def gamma_correction(img, gamma):\n",
            "    res = 255.0 * ((img.astype(float) / 255.0) ** gamma)\n",
            "    return np.clip(res, 0, 255).astype(np.uint8)\n",
            "\n",
            "gray_gamma = gamma_correction(img_gray, 1.5)\n",
            "color_gamma = gamma_correction(img_color, 1.5)\n",
            "show_results(img_color, img_gray, gray_gamma, color_gamma, \"g) Correção Gama\")\n"
        ]
    }
]

notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("03_Atividade_Tecnicas_de_Realce.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("Notebook generated successfully!")
