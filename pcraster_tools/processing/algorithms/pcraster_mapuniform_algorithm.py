# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from pcraster import (
    setclone,
    report,
    mapnormal
)
from qgis.core import (QgsProcessingParameterRasterDestination,
                       QgsProcessingParameterRasterLayer)

from pcraster_tools.processing.algorithm import PCRasterAlgorithm


class PCRasterMapuniformAlgorithm(PCRasterAlgorithm):
    """
    Cells get non spatial value taken from an uniform distribution
    """

    INPUT_CLONE = 'INPUT'
    OUTPUT_MAPUNIFORM = 'OUTPUT'

    def createInstance(self):  # pylint: disable=missing-function-docstring
        return PCRasterMapuniformAlgorithm()

    def name(self):  # pylint: disable=missing-function-docstring
        return 'mapuniform'

    def displayName(self):  # pylint: disable=missing-function-docstring
        return self.tr('mapuniform')

    def group(self):  # pylint: disable=missing-function-docstring
        return self.tr('Map operations')

    def groupId(self):  # pylint: disable=missing-function-docstring
        return 'map'

    def shortHelpString(self):  # pylint: disable=missing-function-docstring
        return self.tr(
            """Cells get non spatial value taken from an uniform distribution

            <a href="https://pcraster.geo.uu.nl/pcraster/4.3.1/documentation/pcraster_manual/sphinx/op_mapuniform.html">PCRaster documentation</a>

            Parameters:

            * <b>Input mask raster layer</b> (required) - Raster layer of any data type with the mask for which the values will be calculated
            * <b>Output uniform raster</b> (required) - scalar raster layer with value assigned from a uniform distribution
            """
        )

    def initAlgorithm(self, config=None):  # pylint: disable=missing-function-docstring,unused-argument
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.INPUT_CLONE,
                self.tr('Mask raster layer')
            )
        )

        self.addParameter(
            QgsProcessingParameterRasterDestination(
                self.OUTPUT_MAPUNIFORM,
                self.tr('Output uniform layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):  # pylint: disable=missing-function-docstring,unused-argument
        input_clone = self.parameterAsRasterLayer(parameters, self.INPUT_CLONE, context)

        setclone(input_clone.dataProvider().dataSourceUri())
        MapUniformLayer = mapnormal()
        outputFilePath = self.parameterAsOutputLayer(parameters, self.OUTPUT_MAPUNIFORM, context)

        report(MapUniformLayer, outputFilePath)

        return {self.OUTPUT_MAPUNIFORM: outputFilePath}
