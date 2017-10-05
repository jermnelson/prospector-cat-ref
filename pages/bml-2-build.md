title: Iteration 2 - Building
published: 2017-10-05

The second development cycle for GoldRush BIBCAT began earlier
in 2017 and implemented a number of changes to how the BIBFRAME 
Linked Data is structured and published to the web for search 
engine crawling. Using this Repository's [Github Issue tracking](https://github.com/KnowledgeLinks/alliance-bibcat/issues), 
bugs and enhancements are entered and tracked through through-out the build phase.




<ol>
<li style="padding-bottom: 1em">
    <p>In the initial step, MARC XML is exported out of the GoldRush&copy; Comparison Tool that includes a 997 field containing the Alliance Match Key.</p>
    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#bml-2-marc-src-dialog">MARC XML</button>
</li>
<li style="padding-bottom: 1em">
    <p>The next step is to iterate through the XML export file and process each MARC XML file by running the XML record through the Library of
     Congress MARC2BIBFRAME2 that uses multiple XSLT files to transform the MARC XML into BIBFRAME 2.0 RDF XML</p>
    <button type="button" class="btn btn-warning" data-toggle="modal" data-target="#bml-2-loc-marc2bf2">LOC Marc2BIBFRAME2 XSLT</button>
<li style="padding-bottom: 1em">
    <p>With the BIBFRAME RDF XML, we then run a process to replace the generated URIs of the largest BIBFRAME Instance and associated BIBFRAME
    Items to use the following patterns with the "slugified" title:</p>
    
    <strong>BIBFRAME Instance:</strong> <em>https://bibcat.coalliance.org/{title-of-instance-in-lowercase-spaces-replaces}</em><br>
    <strong>BIBFRAME Item:</strong><em>https://bibcat.coalliance.org/{title-of-instance-in-lowercase-spaces-replaces}/{institution-name}</em><br>
    <button type="button" class="btn btn-default" data-toggle="modal" data-target="#bml-2-url-sub-dedup">URL Substitution/Dedup</button>
</li>
<li style="padding-bottom: 1em">
    <p>Because of the large number of triples in the Library of Congress output RDF, we then run our first RDF-Map to shrink the total
    number of triples to more manageable size, that is still valid BIBFRAME 2.0</p>
    <button type="button" class="btn btn-success" data-toggle="modal" data-target="#bml-2-loc-bf-to-bf-lean">LOC BF to BF Lean</button>
</li>
<li>
    <p>The final step then runs a SPARQL query and transforms the resulting RDF graph to Schema.org RDF which is then serialized 
    as JSON-LD along with a new landing page.</p>
    <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#bml-2-schema-html">Schema.org/HTML</button></li>
</ol>
