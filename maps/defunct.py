"""collection of scripts that don't work"""


def make_atlas_old(self, at_lay):
    # code that doesn't really work

    # Load template from file

    # grab template file
    with open('', 'r') as templateFile:
        self.templateContent = templateFile.read()

    self.document = QDomDocument()
    self.document.setContent(self.templateContent)

    self.layout = QgsPrintLayout(self.project)
    self.layout.loadFromTemplate(self.document, QgsReadWriteContext(), False)
    self.layout.initializeDefaults()

    # the atlas map
    self.atlas_map = QgsLayoutItemMap(self.layout)
    # self.atlas_map.attemptSetSceneRect(QRectF(20, 20, 130, 130))
    self.atlas_map.setFrameEnabled(True)
    self.atlas_map.setLayers([self.get_layer(at_lay)])
    self.layout.addLayoutItem(self.atlas_map)

    # the atlas
    self.atlas = self.layout.atlas()
    self.atlas.setCoverageLayer(self.get_layer(at_lay))
    self.atlas.setEnabled(True)

    # an overview
    self.overview = QgsLayoutItemMap(self.layout)
    # self.overview.attemptSetSceneRect(QRectF(180, 20, 50, 50))
    self.overview.setFrameEnabled(True)
    self.overview.overview().setLinkedMap(self.atlas_map)
    self.overview.setLayers([self.get_layer(at_lay)])
    self.layout.addLayoutItem(self.overview)
    nextent = QgsRectangle(49670.718, 6415139.086, 699672.519, 7065140.887)
    self.overview.setExtent(nextent)



    # https://gis.stackexchange.com/questions/272774/using-qgis-3-0-api-for-layout

    # for comp in self.projectLayoutManager.printLayouts():
    #     print(comp)
    #     result, error = QgsLayoutExporter.exportToImage(atlas,
    #                                                     baseFilePath='./atlas_out/', extension='.png',
    #                                                     settings=image_settings)
    #     if not result == QgsLayoutExporter.Success:
    #         print(error)

    # # Generate atlas
    # self.atlas.beginRender()
    # self.projectLayoutManager = self.project.layoutManager()
    #
    # self.image_settings = exporter.ImageExportSettings()
    # self.image_settings.dpi = 300  # or whatever you want
    #
    # while self.atlas.next():
    #     self.atlas.prepareForFeature(i)
    #     print(self.atlas.currentFeatureNumber())

    # for i in range(0, self.atlas.numFeatures()):
    #     self.atlas.prepareForFeature(i)
    #     output_jpeg = os.path.join('/.atlas_out/', '% i out.jpeg' % i)
    #     image = self.layout.printPageAsRaster(0)
    #     image.save(output_jpeg)
    #     self.layout.endRender()


    # #grab template file
    # with open('/Users/ewanog/Documents/work/code/repos/humanitarian/hrrp/gp_auto/maps/map_out.qpt', 'r') as templateFile:
    #     self.templateContent = templateFile.read()
    #
    # self.document = QDomDocument()
    # self.document.setContent(self.templateContent)
    #
    # self.composition = QgsLayout(self.project)
    # self.composition.loadFromTemplate(self.document, QgsReadWriteContext(), False)
    #
    # # Get map composition and define scale
    # self.atlasMap = QgsLayoutItemMap(self.composition)
    # self.composition.initializeDefaults()
    # # atlasMap.setNewScale(int(scale))


    # # Setup Atlas
    # atlas = QgsAtlasComposition(composition)
    # atlas.setCoverageLayer(self.get_layer(at_lay))  # Atlas run from desktop_search
    # # atlas.setComposerMap(atlasMap)
    # atlas.setFixedScale(True)
    # atlas.fixedScale()
    # atlas.setHideCoverage(False)
    # atlas.setFilterFeatures(True)
    # atlas.setFeatureFilter("reference = '%s'" % (str(ref)))
    # atlas.setFilterFeatures(True)

   def _create_data_mem_layer(self, nm, header):
        #create an in memory data layer with supplied headers
        vl = QgsVectorLayer('None', nm, 'memory')
        pr = vl.dataProvider()

        # add headers
        pr.addAttributes([QgsField(v, QVariant.String) for v in header])
        vl.updateFields()
        vl.updateExtents()
        print(self._get_layer_col_nms(vl))

        return vl

    def get_map_data(self, uri, sht_nm):
        wb = load_workbook(uri, data_only=True)
        s = wb.get_sheet_by_name(sht_nm)

        vl = self._create_data_mem_layer('data', self._get_xls_row_vals(s[1]))

        #add vals
        attr = vl.dataProvider()
        feat = QgsFeature()

        rs = iter(s.rows)
        next(rs)
        next(rs)
        for r in rs:
            feat.setAttributes(self._get_xls_row_vals(r))
            attr.addFeatures([feat])

        return vl

   def _create_data_mem_layer(self, nm, header):
        #create an in memory data layer with supplied headers
        vl = QgsVectorLayer('None', nm, 'memory')
        pr = vl.dataProvider()

        # add headers
        pr.addAttributes([QgsField(v, QVariant.String) for v in header])
        vl.updateFields()
        vl.updateExtents()
        print(self._get_layer_col_nms(vl))

        return vl

    def get_map_data(self, uri, sht_nm):
        wb = load_workbook(uri, data_only=True)
        s = wb.get_sheet_by_name(sht_nm)

        vl = self._create_data_mem_layer('data', self._get_xls_row_vals(s[1]))

        #add vals
        attr = vl.dataProvider()
        feat = QgsFeature()

        rs = iter(s.rows)
        next(rs)
        next(rs)
        for r in rs:
            feat.setAttributes(self._get_xls_row_vals(r))
            attr.addFeatures([feat])

        return vl

    def set_col_type(self):

        dat.fields()[2].setTypeName('Integer')
        provider = dat.dataProvider()
        updateMap = {}
        fieldIdx = dat.fields().indexFromName('val')
        # features = provider.getFeatures()
        # for feature in features:
        updateMap[feature.id()] = {fieldIdx: 'a'}
        provider.changeAttributeValues(updateMap)

# #show joins:
# lay.vectorJoins()
#
# #good way to do joins:
# import processing
# result = processing.runandload('qgis:joinattributestable', lay, csv, 'HLCIT_CODE', 'HLCIT_CODE', None)
#
# #apply styling to layers:
# l.loadNamedStyle()
#


