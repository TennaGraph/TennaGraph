# Django imports
from django.db import models

# Project imports
from base.models import TimeStampedModel


class EIP(TimeStampedModel):
    """
    Ethereum Improvement Proposals (EIPs) describe standards for the Ethereum platform,
    including core protocol specifications, client APIs, and contract standards.

    """

    """ 
    Type that was not recognized or in not right format 
    """
    OTHER = 'OTHER'

    """ 
    an EIP that is open for consideration 
    """
    DRAFT = 'DRAFT'

    """
    Not documented but it occurs from time to time
    """
    ACTIVE = 'ACTIVE'

    """
    Not documented but it occurs from time to time
    """
    LAST_CALL = 'LAST_CALL'

    """
    Not documented but it occurs from time to time
    """
    REPLACED = 'REPLACED'

    """ 
    an EIP that is planned for immediate adoption, i.e. expected to be included in 
    the next hard fork (for Core/Consensus layer EIPs). 
    """
    ACCEPTED = 'ACCEPTED'

    """
    an EIP that has been adopted in a previous hard fork (for Core/Consensus layer EIPs)
    """
    FINAL = 'FINAL'

    """ 
    an EIP that is not being considered for immediate adoption. 
    May be reconsidered in the future for a subsequent hard fork. 
    """
    DEFERRED = 'DEFERRED'

    PROPOSAL_STATUSES = (
        (DRAFT, 'draft'),
        (ACTIVE, 'active'),
        (LAST_CALL, 'last call'),
        (REPLACED, 'replaced'),
        (ACCEPTED, 'accepted'),
        (FINAL, 'final'),
        (DEFERRED, 'deferred'),
        (OTHER, 'other')
    )


    """ 
    Describes a Ethereum design issue, or provides general guidelines or information to the Ethereum community, 
    but does not propose a new feature. Informational EIPs do not necessarily represent Ethereum community consensus 
    or a recommendation, so users and implementers are free to ignore Informational EIPs or follow their advice. 
    """
    STANDARDS_TRACK = 'STANDARDS_TRACK'

    """ 
    Describes a Ethereum design issue, or provides general guidelines or information to the Ethereum community, 
    but does not propose a new feature. Informational EIPs do not necessarily represent Ethereum community consensus 
    or a recommendation, so users and implementers are free to ignore Informational EIPs or follow their advice. 
    """
    INFORMATIONAL = 'INFORMATIONAL'

    """ 
    Describes a process surrounding Ethereum or proposes a change to (or an event in) a process. 
    Process EIPs are like Standards Track EIPs but apply to areas other than the Ethereum protocol itself. 
    They may propose an implementation, but not to Ethereum's codebase; they often require community consensus; 
    unlike Informational EIPs, they are more than recommendations, and users are typically not free to ignore them. 
    Examples include procedures, guidelines, changes to the decision-making process, and changes to the tools or 
    environment used in Ethereum development. Any meta-EIP is also considered a Process EIP. 
    """
    META = 'META'

    TYPES = (
        (STANDARDS_TRACK, 'standards track'),
        (INFORMATIONAL, 'informational'),
        (META, 'meta'),
        (OTHER, 'other'),
    )


    """ 
    Improvements requiring a consensus fork (e.g. EIP5, EIP101), as well as changes that are not necessarily 
    consensus critical but may be relevant to “core dev” discussions 
    (for example, the miner/node strategy changes 2, 3, and 4 of EIP86). 
    """
    CORE = 'CORE'

    """ 
    Includes improvements around devp2p (EIP8) and Light Ethereum Subprotocol, as well as 
    proposed improvements to network protocol specifications of whisper and swarm. 
    """
    NETWORKING = 'NETWORKING'

    """ 
    Includes improvements around client API/RPC specifications and standards, and also certain 
    language-level standards like method names (EIP6) and contract ABIs. The label “interface” aligns with the 
    interfaces repo and discussion should primarily occur in that repository before 
    an EIP is submitted to the EIPs repository. 
    """
    INTERFACE = 'INTERFACE'

    """ 
    Application-level standards and conventions, including contract standards such as token standards 
    (ERC20), name registries (ERC137), URI schemes (ERC681), library/package formats (EIP190), and wallet formats (EIP85). """
    ERC = 'ERC'

    CATEGORIES = (
        (CORE, 'core'),
        (NETWORKING, 'networking'),
        (INTERFACE, 'Interface'),
        (ERC, 'erc'),
        (OTHER, 'other')
    )

    file_name           = models.CharField(max_length=255)
    file_download_url   = models.URLField()
    file_content        = models.TextField()
    file_sha            = models.CharField(max_length=100)

    eip_num         = models.CharField(max_length=10)
    eip_title       = models.CharField(max_length=225)
    eip_status      = models.CharField(max_length=30, choices=PROPOSAL_STATUSES)
    eip_type        = models.CharField(max_length=30, choices=TYPES)

    # only required for Standard Track
    eip_category    = models.CharField(max_length=30, choices=CATEGORIES, null=True, blank=True)

    # Authors can be in not correct format, so it is parsed as string
    eip_authors     = models.CharField(max_length=255)

    # Date can be in not correct format, so it is parsed as string
    eip_created     = models.CharField(max_length=100)


    def __str__(self):
        return "{}, {}".format(self.eip_num, self.eip_title)


    def update_with_eip(self, new_eip):
        self.file_name          = new_eip.file_name
        self.file_download_url  = new_eip.file_download_url
        self.file_content       = new_eip.file_content
        self.file_sha           = new_eip.file_sha

        self.eip_num            = new_eip.eip_num
        self.eip_title          = new_eip.eip_title
        self.eip_status         = new_eip.eip_status
        self.eip_type           = new_eip.eip_type
        self.eip_category       = new_eip.eip_category
        self.eip_authors        = new_eip.eip_authors

        return self

