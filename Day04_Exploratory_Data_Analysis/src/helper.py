"""
Helper Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 04
"""

import matplotlib.pyplot as plt


def print_heading(title: str) -> None:
    """
    Print formatted section heading.
    """

    line = "=" * 60

    print(f"\n{line}")
    print(title.upper())
    print(line)


def save_chart(file_path) -> None:
    """
    Save chart using professional settings.
    """

    plt.tight_layout()

    plt.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

# ==========================================================
# SAVE CHART
# ==========================================================

import matplotlib.pyplot as plt


def save_chart(file_path: Path) -> None:
    """
    Save matplotlib figure.

    Args:
        file_path: Output image path.
    """

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.tight_layout()

    plt.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()