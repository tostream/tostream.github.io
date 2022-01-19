title: Long execution time
date: 16/12/2021
author: wp.F

# How to dealing with a long execution time sql 

First thing, identify locking and waiting object.We have to make sure if the sql will lock or wait any table.

The easiest way is to extract the explained plan.Normally, you will only get the estimated plan. In Postgresql, you can use "analyze" to execute your sql once and get a real plan with execution time.
*Diff SQL will have diff behaiver, but basically it will show you the sequence and the cost of every step

we can find from the documenation:
"ANALYZE requires only a read lock on the target table, so it can run in parallel with other activity on the table."
which means we can mimic the process without a huge impact to the system.

Second, a bad index and bad constraint can impact the execution time.
Fragmenation is always the first thing of a bad index, we should always aware of that and rebuild the index regularly)especially in a operational DB.