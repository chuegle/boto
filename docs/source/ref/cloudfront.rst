.. ref-cloudfront

==========
cloudfront
==========

A Crash Course in CloudFront in Boto
------------------------------------

This new boto module provides an interface to Amazon's new Content Service, CloudFront.

Caveats:

This module is not well tested.  Paging of distributions is not yet
supported.  CNAME support is completely untested.  Use with caution.
Feedback and bug reports are greatly appreciated.

The following shows the main features of the cloudfront module from an interactive shell:

Create an cloudfront connection:

>>> from boto1.cloudfront import CloudFrontConnection
>>> c = CloudFrontConnection()

Create a new :class:`boto1.cloudfront.distribution.Distribution`:

>>> distro = c.create_distribution(origin='mybucket.s3.amazonaws.com', enabled=False, comment='My new Distribution')
>>> d.domain_name
u'd2oxf3980lnb8l.cloudfront.net'
>>> d.id
u'ECH69MOIW7613'
>>> d.status
u'InProgress'
>>> d.config.comment
u'My new distribution'
>>> d.config.origin
u'mybucket.s3.amazonaws.com'
>>> d.config.caller_reference
u'31b8d9cf-a623-4a28-b062-a91856fac6d0'
>>> d.config.enabled
False

Note that a new caller reference is created automatically, using
uuid.uuid4().  The :class:`boto1.cloudfront.distribution.Distribution`, :class:`boto1.cloudfront.distribution.DistributionConfig` and
:class:`boto1.cloudfront.distribution.DistributionSummary` objects are defined in the :mod:`boto1.cloudfront.distribution`
module.

To get a listing of all current distributions:

>>> rs = c.get_all_distributions()
>>> rs
[<boto1.cloudfront.distribution.DistributionSummary instance at 0xe8d4e0>,
 <boto1.cloudfront.distribution.DistributionSummary instance at 0xe8d788>]

This returns a list of :class:`boto1.cloudfront.distribution.DistributionSummary` objects.  Note that paging
is not yet supported!  To get a :class:`boto1.cloudfront.distribution.DistributionObject` from a
:class:`boto1.cloudfront.distribution.DistributionSummary` object:

>>> ds = rs[1]
>>> distro = ds.get_distribution()
>>> distro.domain_name
u'd2oxf3980lnb8l.cloudfront.net'

To change a property of a distribution object:

>>> distro.comment
u'My new distribution'
>>> distro.update(comment='This is a much better comment')
>>> distro.comment
'This is a much better comment'

You can also enable/disable a distribution using the following
convenience methods:

>>> distro.enable()  # just calls distro.update(enabled=True)

or 

>>> distro.disable()  # just calls distro.update(enabled=False)

The only attributes that can be updated for a Distribution are
comment, enabled and cnames.

To delete a :class:`boto1.cloudfront.distribution.Distribution`:

>>> distro.delete()


boto1.cloudfront
---------------

.. automodule:: boto1.cloudfront
   :members:   
   :undoc-members:

boto1.cloudfront.distribution
----------------------------

.. automodule:: boto1.cloudfront.distribution
   :members:   
   :undoc-members:

boto1.cloudfront.exception
-------------------------

.. automodule:: boto1.cloudfront.exception
   :members:   
   :undoc-members:
