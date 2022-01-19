![charter version: 1](https://img.shields.io/badge/charter%20version-1.0-informational) ![last_update: jan. 18. 2022](https://img.shields.io/badge/last%20update-Jan.%2018%2C%202022-informational)

# HTR-United Reuse Charter
 
HTR-United ambitions to **facilitate the access to open training datasets for automatic transcription models** by providing an environment composed of a collectively elaborated catalog of metadata on training datasets, continuous integration tools and data repositories. HTR-United contents are available on Github.
 
Inspired by the [Heritage Data Reuse Charter](https://datacharter.hypotheses.org/), HTR-United has developed this Reuse Charter in order to declare our clear commitment to the six core principles of Reciprocity, Interoperability, Citability, Openness, Stewardship and Trustworthiness and show how this commitment is reflected in the design and the daily operations of the platform. 
In addition, as a mutual declaration of goodwill, the charter allows us to clarify our expectations regarding the interaction between content providers, users and curators.

## Reciprocity
HTR-United is a platform where content providers are able to meet with content users via a [catalog of metadata](https://github.com/HTR-United/htr-united/blob/master/htr-united.yml) and optional data repositories. Reciprocity is a core value in the design of our service as it gives the opportunity for creators of training data to signal and share their content in a sustainable way and in accordance with the licenses attributed to them, while users are given the possibility to provide feedback and contribute new data. Users of data shared through HTR-United are encouraged to make any improvements available under the same license as originally provided. In data repositories, Github’s issues system is available to facilitate this exchange. When the data is shared elsewhere, explicit contact information is provided along with the metadata.

## Interoperability
Whenever possible, training data is made accessible in open and standardized formats that facilitate their reuse. We specifically encourage providers to use ALTO and PAGE XML formats. The metadata catalog is available in the form of a fully documented, human-readable and serializable YAML file. Hosted on a [Github Repository](https://github.com/HTR-United/htr-united), the metadata catalog can be accessed, enriched, forked or harvested by both providers and users. Continuous integration tools facilitate quality control on the validity of the shared files and the metadata catalog.  

## Citability
To encourage a culture of citation for training datasets, we make our recommended citation model explicit and encourage providers to include in the metadata added to the catalog and in the data repository any relevant contributors along with their roles. In the data repository, we recommend the use of [formated citation files](https://citation-file-format.github.io/).

## Openness
Unless stated otherwise, the content of HTR-United’s metadata catalog, related research output and the continuous integration tools are open and freely available under a Creative Commons CC-BY 4.0 license. This allows anyone to legally and freely access, copy, use, enrich, adapt and re-share the resources. Access to the metadata catalog and the continuous integration tools does not require registration or any other form of giving personal data in return for access. 

When possible, providers are encouraged to use licenses as open as possible and to explicitly state the applicable rights. 

## Stewardship
HTR-United contents (namely the metadata catalog, continuous integration tools and optional data repositories) are deployed via Github, a non-sustainable private enterprise. However, content publicly shared on Github is regularly harvested by the Software Heritage initiative for long-term archiving. 

Providers can modify the content of their data repository, change its visibility or remove it. Overall, we encourage the use of versioning and provide assistance to do so via the [main repository’s issues](https://github.com/HTR-United/htr-united/issues/new). 

Providers are not responsible for the availability of image data when they are hosted and published by other entities, but we encourage them to signal any change compromising the quality of the dataset. 

## Trustworthiness
We encourage providers to include provenance information about the training data they integrate and signal within HTR-United. This includes recognizing the diverse contributor roles to clearly document who participated in the production process in order to ensure its traceability and also to recognize and appropriately credit the many kinds of contributions that the creation of ground truth resources involves.

*The HTR-United Reuse Charter is a living document that evolves with the development of the platform.*
