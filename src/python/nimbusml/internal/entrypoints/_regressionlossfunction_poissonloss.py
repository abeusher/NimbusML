# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
PoissonLoss
"""


from ..utils.entrypoints import Component


def poisson_loss(
        **params):
    """
    **Description**
        Poisson loss.

    """

    entrypoint_name = 'PoissonLoss'
    settings = {}

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='RegressionLossFunction')
    return component
