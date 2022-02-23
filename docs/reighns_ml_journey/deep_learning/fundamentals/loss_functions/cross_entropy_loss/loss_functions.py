from math import log2
from typing import *
from typing import List

import numpy as np
import scipy


def compute_class_probabilities(labels: List[Any]) -> List[float]:
    """Calculate frequency of each class.


    From DSFS book, it mentions that we do not actually care about which label is associated with which probability. Thus it is okay to use a dictionary which does not preserve order.

    Args:
        labels (List[Any]): The labels of the data.

    Returns:
        label_probs (List[float]): The frequency of each class.

    Example:
        >>> labels = ['dog', 'dog', 'cat', 'cat', 'dog'] = [0, 0, 1, 1, 0]
        >>> assert compute_class_probabilities(labels) == [2/5, 3/5] or class_probabilities(labels) == [3/5, 2/5]
    """

    num_samples = len(labels)

    label_count: Dict = {}
    label_probs: List = []

    for label in labels:
        if label not in label_count:
            label_count[label] = 1
        else:
            label_count[label] += 1

    for label, count in label_count.items():

        label_probs.append(count / num_samples)

    return label_probs


def compute_entropy_with_class_probability(
    class_probabilities: List[float],
    epsilon: float = 1e-15,
    log_base: int = 2,
) -> float:
    """The formula for entropy is:
    $$\mathrm{H}(Y)= -\sum _{i=1}^{n}{\mathrm{P}(y_{i})\log \mathrm{P}(y_{i})}$$

    Args:
        class_probabilities (List[float]): Frequency probability of class occurences.

    Returns:
        entropy (float): The entropy of the dataset.

    Example:
        >>> # maximum chaos -> entropy = 1
        >>> class_probabilities = [1/2, 1/2]
        >>> assert compute_entropy_with_class_probability(class_probabilities) == 1
        >>> # minimum chaos -> entropy = 0
        >>> class_probabilities = [1, 0] # or [0, 1]
        >>> assert np.isclose(compute_entropy_with_class_probability(class_probabilities), 0)
        >>> class_probabilities = [2/5, 3/5]
        >>> assert compute_entropy_with_class_probability(class_probabilities) == 0.9709505944546686
    """

    assert (
        np.sum(class_probabilities) == 1
    ), f"Probabilities do not sum to 1 and is {np.sum(class_probabilities)}!"

    assert log_base in [
        2,
        10,
    ], f"log_base must be either 2 or 10. Got {log_base}!"

    if log_base == 2:
        log_fn = getattr(np, "log2")
    else:
        log_fn = getattr(np, "log10")

    entropy = 0
    for y in class_probabilities:
        if y == 0:
            y = epsilon
        entropy += y * log_fn(y)
    entropy = -1 * entropy

    return entropy


def compute_entropy_with_class_labels(
    labels: List[Any], *args, **kwargs
) -> float:
    """Compute the entropy of the dataset given class labels.

    Args:
        labels (List[Any]): The labels of the data.

    Returns:
        entropy (float): The entropy of the dataset.

    Example:
        >>> from scipy.stats import entropy
        >>> labels = [0, 0, 1, 1, 0] # ['dog', 'dog', 'cat', 'cat', 'dog']
        >>> # Note scipy's entropy takes in class freq
        >>> compute_entropy_with_class_labels(labels=labels, epsilon=1e-15, log_base=2) == entropy([3/5, 2/5], base=2)
    """

    return compute_entropy_with_class_probability(
        compute_class_probabilities(labels), *args, **kwargs
    )
