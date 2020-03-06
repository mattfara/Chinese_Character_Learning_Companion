<xsl:transform version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output omit-xml-declaration="yes"/>
  <xsl:variable name="new_line" select="'&#xA;'" />
  <xsl:variable name="comma" select="', '"/>
  <xsl:variable name="zero-width-space" select="'&#8203;'"/>
  <xsl:template match="/">
    <xsl:apply-templates select=".//*[@class='head']"/>
  </xsl:template>

  <xsl:template match="*[@class='head']">
    <xsl:value-of select=".//*[@class='hanzi']"/>
    <xsl:text> (</xsl:text>
    <xsl:apply-templates select=".//*[@class='pinyin']"/>
    <xsl:text>)</xsl:text>
    <xsl:text>: </xsl:text>
    <xsl:apply-templates select="following-sibling::*[@class='details']"/>
  </xsl:template>

  <xsl:template match="*[@class='details']">
    <xsl:value-of select="normalize-space(.)"/><xsl:value-of select="$new_line"/>
  </xsl:template>

  <xsl:template match="*[@class='pinyin']">
    <xsl:value-of select="replace(., $zero-width-space, '')"/>
  </xsl:template>
</xsl:transform>
