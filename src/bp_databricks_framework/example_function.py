"""Use this template to implement your Spark DataFrame transform functions
All transform functions take Spark DataFrame or Spark temporary view as input
and return result Spark DataFrame and/or a temporary view. The input and output
is handled by the decorator function df_input_output_wrapper. You just focus on
implementing your own logic and don't worry about if you need to create view.
"""

import os

from pyspark.sql import DataFrame
from loguru import logger

from admcore.cbc.common.functions.common_functions import df_input_output_wrapper
import admcore.utils as ut


# pylint: disable="W0613"
@df_input_output_wrapper
def your_transform_function(
    df: DataFrame,
    func_conf,
    action_conf,
    task_conf,
    pl_conf
) -> DataFrame:
    """Your function has to follow the same function declaration. 
    And the positional arguments have to be in the same order as this example.

    Args:
        df (DataFrame): Spark dataframe passed from upstream Functions. Could be None.
        func_conf (_type_): Function configuration part in YAML config file
        action_conf (_type_): Function configuration part in YAML config file
        task_conf (_type_, optional): The entire task configuration in YAML config file
        pl_conf (_type_, optional): All configuration in pipeline.yml file

    Returns:
        DataFrame: Spark dataframe
    """
    logger.info("This is my customized ADM function")

    # Example: Get Spark session
    sp = ut.AdmSpark.get_spark_session()

    # Example Get project/compute level variables in src/env.toml file
    table_name = f"{os.getenv('MFL_CAT_MFL_BRONZE')}.external_files.mfl_tps_sysco_ca"

    # Example: Get session level variables
    batch_id = pl_conf.session_variables.batch_id

    return df
