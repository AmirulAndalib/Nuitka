# pylint: disable=I0021,too-many-lines
# pylint: disable=I0021,line-too-long

"""Children having mixins

WARNING, this code is GENERATED. Modify the template ChildrenHavingMixin.py.j2 instead!

spell-checker: ignore capitalize casefold center clear copy count decode encode endswith expandtabs find format formatmap get haskey hex index isalnum isalpha isascii isdecimal isdigit isidentifier islower isnumeric isprintable isspace istitle isupper items iteritems iterkeys itervalues join keys ljust lower lstrip maketrans partition pop popitem replace rfind rindex rjust rpartition rsplit rstrip setdefault split splitlines startswith strip swapcase title translate update upper values viewitems viewkeys viewvalues zfill
spell-checker: ignore args chars count default encoding end errors fillchar iterable keepends key maxsplit new old pairs prefix sep start sub suffix table tabsize width
"""


# Loop unrolling over child names, pylint: disable=too-many-branches

from .NodeBases import NodeBase
from .NodeMakingHelpers import wrapExpressionWithSideEffects


class ChildrenHavingDistMixin(object):
    # Mixins are not allow to specify slots, pylint: disable=assigning-non-slot
    __slots__ = ()

    named_children = ("dist",)

    checkers = {}

    def __init__(
        self,
        dist,
    ):
        if "dist" in self.checkers:
            dist = self.checkers["dist"](dist)

        if type(dist) is tuple:
            for val in dist:
                assert val is not None, "dist"

                val.parent = self
        elif dist is None:
            pass
        else:
            dist.parent = self

        self.subnode_dist = dist

    def setChild(self, name, value):
        """Set a child value.

        Do not overload, provider self.checkers instead.
        """
        # Only accept legal child names
        assert name in self.named_children, name

        # Lists as inputs are OK, but turn them into tuples.
        if type(value) is list:
            value = tuple(value)

        if name in self.checkers:
            value = self.checkers[name](value)

        # Re-parent value to us.
        if type(value) is tuple:
            for val in value:
                val.parent = self
        elif value is not None:
            value.parent = self

        attr_name = "subnode_" + name

        # Determine old value, and inform it about losing its parent.
        old_value = getattr(self, attr_name)

        assert old_value is not value, value

        setattr(self, attr_name, value)

    def clearChild(self, name):
        # Only accept legal child names
        assert name in ("dist",), name

        if name in self.checkers:
            self.checkers[name](None)

        # Determine old value, and check it has no parent anymore.
        old_value = self.subnode_dist
        assert old_value is not None
        assert old_value.parent is None
        self.subnode_dist = None

    def getChild(self, name):
        attr_name = "subnode_" + name
        return getattr(self, attr_name)

    def getVisitableNodes(self):
        """The visitable nodes, with tuple values flattened."""

        value = self.subnode_dist

        if value is None:
            return ()
        else:
            return (value,)

    def getVisitableNodesNamed(self):
        """Named children dictionary.

        For use in cloning nodes, debugging and XML output.
        """

        return (("dist", self.subnode_dist),)

    def replaceChild(self, old_node, new_node):
        if new_node is not None and not isinstance(new_node, NodeBase):
            raise AssertionError(
                "Cannot replace with", new_node, "old", old_node, "in", self
            )
        value = self.subnode_dist
        # Find the replaced node, as an added difficulty, what might be
        # happening, is that the old node is an element of a tuple, in which we
        # may also remove that element, by setting it to None.

        if old_node is value:
            new_node.parent = self
            self.subnode_dist = new_node
        else:
            raise AssertionError("Didn't find child", old_node, "in", self)

    def getCloneArgs(self):
        """Get clones of all children to pass for a new node.

        Needs to make clones of child nodes too.
        """

        value = self.subnode_dist

        values = {"dist": value.makeClone()}
        values.update(self.getDetails())

        return values

    def finalize(self):
        del self.parent

        self.subnode_dist.finalize()

    def computeExpressionRaw(self, trace_collection):
        """Compute an expression.

        Default behavior is to just visit the child expressions first, and
        then the node "computeExpression". For a few cases this needs to
        be overloaded, e.g. conditional expressions.
        """

        # First apply the sub-expression, as they it's evaluated before.
        value = self.subnode_dist

        if value is not None:
            expression = trace_collection.onExpression(expression)

            if expression.willRaiseException(BaseException):
                return (
                    expression,
                    "new_raise",
                    lambda: "For '%s' the child expression '%s' will raise."
                    % (self.getChildNameNice(), expression.getChildNameNice()),
                )

        # Then ask ourselves to work on it.
        return self.computeExpression(trace_collection)


class ChildrenHavingDistributionNameMixin(object):
    # Mixins are not allow to specify slots, pylint: disable=assigning-non-slot
    __slots__ = ()

    named_children = ("distribution_name",)

    checkers = {}

    def __init__(
        self,
        distribution_name,
    ):
        if "distribution_name" in self.checkers:
            distribution_name = self.checkers["distribution_name"](distribution_name)

        if type(distribution_name) is tuple:
            for val in distribution_name:
                assert val is not None, "distribution_name"

                val.parent = self
        elif distribution_name is None:
            pass
        else:
            distribution_name.parent = self

        self.subnode_distribution_name = distribution_name

    def setChild(self, name, value):
        """Set a child value.

        Do not overload, provider self.checkers instead.
        """
        # Only accept legal child names
        assert name in self.named_children, name

        # Lists as inputs are OK, but turn them into tuples.
        if type(value) is list:
            value = tuple(value)

        if name in self.checkers:
            value = self.checkers[name](value)

        # Re-parent value to us.
        if type(value) is tuple:
            for val in value:
                val.parent = self
        elif value is not None:
            value.parent = self

        attr_name = "subnode_" + name

        # Determine old value, and inform it about losing its parent.
        old_value = getattr(self, attr_name)

        assert old_value is not value, value

        setattr(self, attr_name, value)

    def clearChild(self, name):
        # Only accept legal child names
        assert name in ("distribution_name",), name

        if name in self.checkers:
            self.checkers[name](None)

        # Determine old value, and check it has no parent anymore.
        old_value = self.subnode_distribution_name
        assert old_value is not None
        assert old_value.parent is None
        self.subnode_distribution_name = None

    def getChild(self, name):
        attr_name = "subnode_" + name
        return getattr(self, attr_name)

    def getVisitableNodes(self):
        """The visitable nodes, with tuple values flattened."""

        value = self.subnode_distribution_name

        if value is None:
            return ()
        else:
            return (value,)

    def getVisitableNodesNamed(self):
        """Named children dictionary.

        For use in cloning nodes, debugging and XML output.
        """

        return (("distribution_name", self.subnode_distribution_name),)

    def replaceChild(self, old_node, new_node):
        if new_node is not None and not isinstance(new_node, NodeBase):
            raise AssertionError(
                "Cannot replace with", new_node, "old", old_node, "in", self
            )
        value = self.subnode_distribution_name
        # Find the replaced node, as an added difficulty, what might be
        # happening, is that the old node is an element of a tuple, in which we
        # may also remove that element, by setting it to None.

        if old_node is value:
            new_node.parent = self
            self.subnode_distribution_name = new_node
        else:
            raise AssertionError("Didn't find child", old_node, "in", self)

    def getCloneArgs(self):
        """Get clones of all children to pass for a new node.

        Needs to make clones of child nodes too.
        """

        value = self.subnode_distribution_name

        values = {"distribution_name": value.makeClone()}
        values.update(self.getDetails())

        return values

    def finalize(self):
        del self.parent

        self.subnode_distribution_name.finalize()

    def computeExpressionRaw(self, trace_collection):
        """Compute an expression.

        Default behavior is to just visit the child expressions first, and
        then the node "computeExpression". For a few cases this needs to
        be overloaded, e.g. conditional expressions.
        """

        # First apply the sub-expression, as they it's evaluated before.
        value = self.subnode_distribution_name

        if value is not None:
            expression = trace_collection.onExpression(expression)

            if expression.willRaiseException(BaseException):
                return (
                    expression,
                    "new_raise",
                    lambda: "For '%s' the child expression '%s' will raise."
                    % (self.getChildNameNice(), expression.getChildNameNice()),
                )

        # Then ask ourselves to work on it.
        return self.computeExpression(trace_collection)


class ChildrenHavingElementsTupleMixin(object):
    # Mixins are not allow to specify slots, pylint: disable=assigning-non-slot
    __slots__ = ()

    named_children = ("elements",)

    checkers = {}

    def __init__(
        self,
        elements,
    ):
        if "elements" in self.checkers:
            elements = self.checkers["elements"](elements)

        if type(elements) is tuple:
            for val in elements:
                assert val is not None, "elements"

                val.parent = self
        elif elements is None:
            pass
        else:
            elements.parent = self

        self.subnode_elements = elements

    def setChild(self, name, value):
        """Set a child value.

        Do not overload, provider self.checkers instead.
        """
        # Only accept legal child names
        assert name in self.named_children, name

        # Lists as inputs are OK, but turn them into tuples.
        if type(value) is list:
            value = tuple(value)

        if name in self.checkers:
            value = self.checkers[name](value)

        # Re-parent value to us.
        if type(value) is tuple:
            for val in value:
                val.parent = self
        elif value is not None:
            value.parent = self

        attr_name = "subnode_" + name

        # Determine old value, and inform it about losing its parent.
        old_value = getattr(self, attr_name)

        assert old_value is not value, value

        setattr(self, attr_name, value)

    def clearChild(self, name):
        # Only accept legal child names
        assert name in ("elements",), name

        if name in self.checkers:
            self.checkers[name](None)

        # Determine old value, and check it has no parent anymore.
        old_value = self.subnode_elements
        assert old_value is not None
        assert old_value.parent is None
        self.subnode_elements = None

    def getChild(self, name):
        attr_name = "subnode_" + name
        return getattr(self, attr_name)

    def getVisitableNodes(self):
        """The visitable nodes, with tuple values flattened."""

        return self.subnode_elements

    def getVisitableNodesNamed(self):
        """Named children dictionary.

        For use in cloning nodes, debugging and XML output.
        """

        return (("elements", self.subnode_elements),)

    def replaceChild(self, old_node, new_node):
        if new_node is not None and not isinstance(new_node, NodeBase):
            raise AssertionError(
                "Cannot replace with", new_node, "old", old_node, "in", self
            )
        value = self.subnode_elements
        if old_node not in value:
            raise AssertionError("Didn't find child", old_node, "in", self)

        if new_node is not None:
            new_value = tuple(
                (val if val is not old_node else new_node) for val in value
            )
        else:
            new_value = tuple(val for val in value if val is not old_node)

        new_node.parent = self

        self.subnode_elements = new_value

    def getCloneArgs(self):
        """Get clones of all children to pass for a new node.

        Needs to make clones of child nodes too.
        """

        value = self.subnode_elements

        values = {"elements": tuple(v.makeClone() for v in value)}
        values.update(self.getDetails())

        return values

    def finalize(self):
        del self.parent

        for c in self.subnode_elements:
            c.finalize()

    def computeExpressionRaw(self, trace_collection):
        """Compute an expression.

        Default behavior is to just visit the child expressions first, and
        then the node "computeExpression". For a few cases this needs to
        be overloaded, e.g. conditional expressions.
        """

        # First apply the sub-expressions, as they are evaluated before
        # the actual operation.
        for count, sub_expression in enumerate(self.subnode_elements):
            expression = trace_collection.onExpression(sub_expression)

            if expression.willRaiseException(BaseException):
                sub_expressions = self.getVisitableNodes()

                wrapped_expression = wrapExpressionWithSideEffects(
                    side_effects=sub_expressions[:count],
                    old_node=sub_expression,
                    new_node=expression,
                )

                return (
                    wrapped_expression,
                    "new_raise",
                    lambda: "For '%s' the child expression '%s' will raise."
                    % (self.getChildNameNice(), expression.getChildNameNice()),
                )

        # Then ask ourselves to work on it.
        return self.computeExpression(trace_collection)


class ChildrenHavingGroupNameMixin(object):
    # Mixins are not allow to specify slots, pylint: disable=assigning-non-slot
    __slots__ = ()

    named_children = ("group", "name")

    checkers = {}

    def __init__(
        self,
        group,
        name,
    ):
        if "group" in self.checkers:
            group = self.checkers["group"](group)

        if type(group) is tuple:
            for val in group:
                assert val is not None, "group"

                val.parent = self
        elif group is None:
            pass
        else:
            group.parent = self

        self.subnode_group = group
        if "name" in self.checkers:
            name = self.checkers["name"](name)

        if type(name) is tuple:
            for val in name:
                assert val is not None, "name"

                val.parent = self
        elif name is None:
            pass
        else:
            name.parent = self

        self.subnode_name = name

    def setChild(self, name, value):
        """Set a child value.

        Do not overload, provider self.checkers instead.
        """
        # Only accept legal child names
        assert name in self.named_children, name

        # Lists as inputs are OK, but turn them into tuples.
        if type(value) is list:
            value = tuple(value)

        if name in self.checkers:
            value = self.checkers[name](value)

        # Re-parent value to us.
        if type(value) is tuple:
            for val in value:
                val.parent = self
        elif value is not None:
            value.parent = self

        attr_name = "subnode_" + name

        # Determine old value, and inform it about losing its parent.
        old_value = getattr(self, attr_name)

        assert old_value is not value, value

        setattr(self, attr_name, value)

    def clearChild(self, name):
        # Only accept legal child names
        assert name in ("group", "name"), name

        if name in self.checkers:
            self.checkers[name](None)

        # Determine old value, and check it has no parent anymore.
        attr_name = "subnode_" + name
        # Determine old value, and inform it about losing its parent.
        old_value = getattr(self, attr_name)
        assert old_value is not None
        assert old_value.parent is None

        setattr(self, attr_name, None)

    def getChild(self, name):
        attr_name = "subnode_" + name
        return getattr(self, attr_name)

    def getVisitableNodes(self):
        """The visitable nodes, with tuple values flattened."""

        result = []

        value = self.subnode_group

        if value is None:
            pass
        elif type(value) is tuple:
            result.extend(value)
        else:
            assert isinstance(value, NodeBase), (
                "has illegal child",
                "group",
                value,
                value.__class__,
            )
            result.append(value)

        value = self.subnode_name

        if value is None:
            pass
        elif type(value) is tuple:
            result.extend(value)
        else:
            assert isinstance(value, NodeBase), (
                "has illegal child",
                "name",
                value,
                value.__class__,
            )
            result.append(value)

        return tuple(result)

    def getVisitableNodesNamed(self):
        """Named children dictionary.

        For use in cloning nodes, debugging and XML output.
        """

        return (
            ("group", self.subnode_group),
            ("name", self.subnode_name),
        )

    def replaceChild(self, old_node, new_node):
        if new_node is not None and not isinstance(new_node, NodeBase):
            raise AssertionError(
                "Cannot replace with", new_node, "old", old_node, "in", self
            )
        # Find the replaced node, as an added difficulty, what might be
        # happening, is that the old node is an element of a tuple, in which we
        # may also remove that element, by setting it to None.
        value = self.subnode_group

        if value is None:
            pass
        elif type(value) is tuple:
            if old_node in value:
                if new_node is not None:
                    self.setChild(
                        "group",
                        tuple(
                            (val if val is not old_node else new_node) for val in value
                        ),
                    )
                else:
                    self.setChild(
                        "group", tuple(val for val in value if val is not old_node)
                    )

                return "group"
        else:
            assert isinstance(value, NodeBase), (
                "has illegal child",
                "group",
                value,
                value.__class__,
            )

            if old_node is value:
                self.setChild("group", new_node)

                return "group"

        value = self.subnode_name

        if value is None:
            pass
        elif type(value) is tuple:
            if old_node in value:
                if new_node is not None:
                    self.setChild(
                        "name",
                        tuple(
                            (val if val is not old_node else new_node) for val in value
                        ),
                    )
                else:
                    self.setChild(
                        "name", tuple(val for val in value if val is not old_node)
                    )

                return "name"
        else:
            assert isinstance(value, NodeBase), (
                "has illegal child",
                "name",
                value,
                value.__class__,
            )

            if old_node is value:
                self.setChild("name", new_node)

                return "name"

        raise AssertionError("Didn't find child", old_node, "in", self)

    def getCloneArgs(self):
        """Get clones of all children to pass for a new node.

        Needs to make clones of child nodes too.
        """

        values = {}

        value = self.subnode_group

        if value is None:
            values["group"] = None
        elif type(value) is tuple:
            values["group"] = tuple(v.makeClone() for v in value)
        else:
            values["group"] = value.makeClone()
        value = self.subnode_name

        if value is None:
            values["name"] = None
        elif type(value) is tuple:
            values["name"] = tuple(v.makeClone() for v in value)
        else:
            values["name"] = value.makeClone()

        values.update(self.getDetails())

        return values

    def finalize(self):
        del self.parent

        if self.subnode_group is not None:
            self.subnode_group.finalize()
        if self.subnode_name is not None:
            self.subnode_name.finalize()

    def computeExpressionRaw(self, trace_collection):
        """Compute an expression.

        Default behavior is to just visit the child expressions first, and
        then the node "computeExpression". For a few cases this needs to
        be overloaded, e.g. conditional expressions.
        """

        # First apply the sub-expressions, as they are evaluated before
        # the actual operation.
        for count, sub_expression in enumerate(self.getVisitableNodes()):
            expression = trace_collection.onExpression(sub_expression)

            if expression.willRaiseException(BaseException):
                sub_expressions = self.getVisitableNodes()

                wrapped_expression = wrapExpressionWithSideEffects(
                    side_effects=sub_expressions[:count],
                    old_node=sub_expression,
                    new_node=expression,
                )

                return (
                    wrapped_expression,
                    "new_raise",
                    lambda: "For '%s' the child expression '%s' will raise."
                    % (self.getChildNameNice(), expression.getChildNameNice()),
                )

        # Then ask ourselves to work on it.
        return self.computeExpression(trace_collection)


class ChildrenHavingRequirementsTupleMixin(object):
    # Mixins are not allow to specify slots, pylint: disable=assigning-non-slot
    __slots__ = ()

    named_children = ("requirements",)

    checkers = {}

    def __init__(
        self,
        requirements,
    ):
        if "requirements" in self.checkers:
            requirements = self.checkers["requirements"](requirements)

        if type(requirements) is tuple:
            for val in requirements:
                assert val is not None, "requirements"

                val.parent = self
        elif requirements is None:
            pass
        else:
            requirements.parent = self

        self.subnode_requirements = requirements

    def setChild(self, name, value):
        """Set a child value.

        Do not overload, provider self.checkers instead.
        """
        # Only accept legal child names
        assert name in self.named_children, name

        # Lists as inputs are OK, but turn them into tuples.
        if type(value) is list:
            value = tuple(value)

        if name in self.checkers:
            value = self.checkers[name](value)

        # Re-parent value to us.
        if type(value) is tuple:
            for val in value:
                val.parent = self
        elif value is not None:
            value.parent = self

        attr_name = "subnode_" + name

        # Determine old value, and inform it about losing its parent.
        old_value = getattr(self, attr_name)

        assert old_value is not value, value

        setattr(self, attr_name, value)

    def clearChild(self, name):
        # Only accept legal child names
        assert name in ("requirements",), name

        if name in self.checkers:
            self.checkers[name](None)

        # Determine old value, and check it has no parent anymore.
        old_value = self.subnode_requirements
        assert old_value is not None
        assert old_value.parent is None
        self.subnode_requirements = None

    def getChild(self, name):
        attr_name = "subnode_" + name
        return getattr(self, attr_name)

    def getVisitableNodes(self):
        """The visitable nodes, with tuple values flattened."""

        return self.subnode_requirements

    def getVisitableNodesNamed(self):
        """Named children dictionary.

        For use in cloning nodes, debugging and XML output.
        """

        return (("requirements", self.subnode_requirements),)

    def replaceChild(self, old_node, new_node):
        if new_node is not None and not isinstance(new_node, NodeBase):
            raise AssertionError(
                "Cannot replace with", new_node, "old", old_node, "in", self
            )
        value = self.subnode_requirements
        if old_node not in value:
            raise AssertionError("Didn't find child", old_node, "in", self)

        if new_node is not None:
            new_value = tuple(
                (val if val is not old_node else new_node) for val in value
            )
        else:
            new_value = tuple(val for val in value if val is not old_node)

        new_node.parent = self

        self.subnode_requirements = new_value

    def getCloneArgs(self):
        """Get clones of all children to pass for a new node.

        Needs to make clones of child nodes too.
        """

        value = self.subnode_requirements

        values = {"requirements": tuple(v.makeClone() for v in value)}
        values.update(self.getDetails())

        return values

    def finalize(self):
        del self.parent

        for c in self.subnode_requirements:
            c.finalize()

    def computeExpressionRaw(self, trace_collection):
        """Compute an expression.

        Default behavior is to just visit the child expressions first, and
        then the node "computeExpression". For a few cases this needs to
        be overloaded, e.g. conditional expressions.
        """

        # First apply the sub-expressions, as they are evaluated before
        # the actual operation.
        for count, sub_expression in enumerate(self.subnode_requirements):
            expression = trace_collection.onExpression(sub_expression)

            if expression.willRaiseException(BaseException):
                sub_expressions = self.getVisitableNodes()

                wrapped_expression = wrapExpressionWithSideEffects(
                    side_effects=sub_expressions[:count],
                    old_node=sub_expression,
                    new_node=expression,
                )

                return (
                    wrapped_expression,
                    "new_raise",
                    lambda: "For '%s' the child expression '%s' will raise."
                    % (self.getChildNameNice(), expression.getChildNameNice()),
                )

        # Then ask ourselves to work on it.
        return self.computeExpression(trace_collection)
