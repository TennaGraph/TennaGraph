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
    an EIP that is open for consideration 
    """
    DRAFT = 'DRAFT'

    """
    Not documented but it occurs from time to time
    """
    ACTIVE = 'ACTIVE'

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

    PROPOSAL_STATUS = (
        (DRAFT, 'draft'),
        (ACTIVE, 'active'),
        (ACCEPTED, 'accepted'),
        (FINAL, 'final'),
        (DEFERRED, 'deferred'),
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

    """ 
    Type that was not recognized or in not right format 
    """
    OTHER = 'OTHER'

    CATEGORIES = (
        (CORE, 'core'),
        (NETWORKING, 'networking'),
        (INTERFACE, 'Interface'),
        (ERC, 'erc'),
        (INFORMATIONAL, 'informational'),
        (META, 'meta'),
        (OTHER, 'other'),
    )


    file_name           = models.CharField(max_length=255)
    file_download_url   = models.URLField()
    file_content        = models.TextField()

    eip_num         = models.CharField(max_length=10)
    eip_title       = models.CharField(max_length=225)
    eip_status      = models.CharField(max_length=30, choices=PROPOSAL_STATUS)
    eip_category    = models.CharField(max_length=30, choices=CATEGORIES)

    # Authors can be in not correct format, so it is parsed as string
    eip_authors     = models.CharField(max_length=100)

    # Date can be in not correct format, so it is parsed as string
    eip_created     = models.CharField(max_length=100)
