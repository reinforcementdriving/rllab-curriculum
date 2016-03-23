from rllab.algo.base import RLAlgorithm
from rllab.misc.ext import compact
import lasagne.updates
from rllab.misc import autoargs
from rllab.misc import ext
from functools import partial


# def parse_update_method(update_method, **kwargs):
#     if update_method == 'adam':
#         return partial(
#             lasagne.updates.adam,
#             **compact(ext.extract_dict(
#                 kwargs,
#                 "learning_rate", "beta1", "beta2", "epsilon"
#             ))
#         )
#     elif update_method == 'sgd':
#         return partial(
#             lasagne.updates.sgd, **compact(kwargs))
#     else:
#         raise NotImplementedError
#
#
# class FirstOrderMethod(RLAlgorithm):
#     """
#     Methods that perform online updates without using an optimizer like l-bfgs.
#     This is mostly a stub to handle the hyper-parameters passed to the
#     underlying online optimization algorithm (e.g. learning rate, rho for
#     rmsprop, etc.)
#     """
#
#     def __init__(
#             self,
#             update_method='sgd',
#             learning_rate=0.01,
#             **kwargs):
#         self.update_method = parse_update_method(
#             update_method,
#             learning_rate=learning_rate
#         )
