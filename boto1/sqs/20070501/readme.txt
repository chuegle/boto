The main SQS implementation now uses the 2008-01-01 API verson.  To use the older API version
(2007-05-01) you need to edit your /etc/boto1.cfg or ~/.boto file to add the following line:

boto1.sqs_extend = 20070501

This will allow the code in the boto1.sqs.20070501 module to override the code in boto1.sqs.
