# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
SsaSpikeDetector
"""

__all__ = ["SsaSpikeDetector"]


from ...entrypoints.timeseriesprocessingentrypoints_ssaspikedetector import \
    timeseriesprocessingentrypoints_ssaspikedetector
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignature


class SsaSpikeDetector(BasePipelineItem, DefaultSignature):
    """

    This transform detects the spikes in a seasonal time-series using
    Singular Spectrum Analysis (SSA).

    .. remarks::
        `Singular Spectrum Analysis (SSA)
        <https://en.wikipedia.org/wiki/Singular_spectrum_analysis>`_ is a
        powerful
        framework for decomposing the time-series into trend, seasonality and
        noise components as well as forecasting
        the future values of the time-series. In order to remove the effect
        of such components on anomaly detection,
        this transform adds SSA as a time-series modeler component in the
        detection pipeline.

        The SSA component will be trained and it predicts the next expected
        value on the time-series under normal condition; this expected value
        is
        further used to calculate the amount of deviation from the normal
        (predicted) behavior at that timestamp.
        The distribution of this deviation is then modeled using `Adaptive
        kernel density estimation
        <https://en.wikipedia.org/wiki/Variable_kernel_density_estimation>`_.

        The `p-value <https://en.wikipedia.org/wiki/P-value`_> score for the
        current deviation is calculated based on the
        estimated distribution. The lower its value, the more likely the
        current point is an outlier.

    :param training_window_size: The number of points, N, from the beginning
        of the sequence used to train the SSA
        model.

    :param confidence: The confidence for spike detection in the range [0,
        100].

    :param seasonal_window_size: An upper bound, L,  on the largest relevant
        seasonality in the input time-series, which
        also determines the order of the autoregression of SSA. It must
        satisfy 2 < L < N/2.

    :param side: The argument that determines whether to detect positive or
        negative anomalies, or both. Available
        options are {``Positive``, ``Negative``, ``TwoSided``}.

    :param pvalue_history_length: The size of the sliding window for computing
        the p-value.

    :param error_function: The function used to compute the error between the
        expected and the observed value. Possible
        values are {``SignedDifference``, ``AbsoluteDifference``,
        ``SignedProportion``, ``AbsoluteProportion``,
        ``SquaredDifference``}.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`IIDChangePointDetector
        <nimbusml.preprocessing.timeseries.IIDChangePointDetector>`,
        :py:func:`IIDSpikeDetector
        <nimbusml.preprocessing.timeseries.IIDSpikeDetector>`,
        :py:func:`SsaChangePointDetector
        <nimbusml.preprocessing.timeseries.SsaChangePointDetector>`.

    .. index:: models, timeseries, transform

    Example:
       .. literalinclude:: /../nimbusml/examples/SsaSpikeDetector_df.py
              :language: python
    """

    @trace
    def __init__(
            self,
            training_window_size=100,
            confidence=99.0,
            seasonal_window_size=10,
            side='TwoSided',
            pvalue_history_length=100,
            error_function='SignedDifference',
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.training_window_size = training_window_size
        self.confidence = confidence
        self.seasonal_window_size = seasonal_window_size
        self.side = side
        self.pvalue_history_length = pvalue_history_length
        self.error_function = error_function

    @property
    def _entrypoint(self):
        return timeseriesprocessingentrypoints_ssaspikedetector

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            source=self.source,
            name=self._name_or_source,
            training_window_size=self.training_window_size,
            confidence=self.confidence,
            seasonal_window_size=self.seasonal_window_size,
            side=self.side,
            pvalue_history_length=self.pvalue_history_length,
            error_function=self.error_function)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
